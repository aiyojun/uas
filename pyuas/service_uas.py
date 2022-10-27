import mimetypes
import os
import json
import logging
import argparse
from functools import partial

from tornado import gen
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer

import hashlib
import uuid as uuid_pack
from pymongo import MongoClient


def arg_help():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', default=8000, help='port of service')
    parser.add_argument('-s', '--services', default="services.json", help='services mapping')
    parser.add_argument('-M', '--mongodb', default="127.0.0.1:27017", help='mongodb connection')
    return parser.parse_args()


logging.basicConfig(
    format='%(asctime)s [%(threadName)s] [%(name)s] [%(levelname)s] %(filename)s[line:%(lineno)d] %(message)s',
    level=logging.INFO
)
args = arg_help()


UAS_SIGN = 'uas'
UAS_USERS = 'users'
UAS_LOGIN = 'login_records'


def md5(s):
    return hashlib.md5(s.encode(encoding='utf-8')).hexdigest()


def uuid():
    return str(uuid_pack.uuid1()).replace("-", "")


class UserManager:
    data_source = None
    login_records = None

    def __init__(self, mongodb):
        self.data_source = MongoClient(mongodb)[UAS_SIGN][UAS_USERS]
        self.login_records = MongoClient(mongodb)[UAS_SIGN][UAS_LOGIN]

    def add_user(self, user):
        if "username" not in user:
            raise Exception("Lack of username.")
        if "password" not in user:
            raise Exception("Lack of password.")
        user["password"] = md5(user["password"])
        user_token = uuid()
        user["id"] = user_token
        self.data_source.insert_one(user)
        return user_token

    def register_user_by_email(self, email, password):
        return self.add_user({"username": "", "password": password, "email": email})

    def modify_password_by_email(self, email, new_password):
        cursor = self.data_source.find({"email": email}, {"_id": 0})
        users = []
        for every in cursor:
            users.append(every)
        if len(users) == 0:
            return
        users[0]['password'] = new_password

    def find_by_id(self, user_token):
        cursor = self.data_source.find({"id": user_token}, {"_id": 0})
        rs = []
        for every in cursor:
            rs.append(every)
        if len(rs) == 0:
            return None
        return rs[0]

    def find_by_name(self, username):
        users = []
        cursor = self.data_source.find({"username": username}, {"_id": 0})
        for every in cursor:
            users.append(every)
        return users

    def find_by_email(self, email):
        cursor = self.data_source.find({"email": email}, {"_id": 0})
        users = []
        for every in cursor:
            users.append(every)
        return users[0] if len(users) != 0 else None

    def validate(self, token, service_id):
        record = []
        cursor = self.login_records.find({"token": token}, {"_id": 0})
        for every in cursor:
            record.append(every)
        if len(record) == 0:
            raise Exception("No such token!")
        user = []
        cursor = self.data_source.find({"email": record[0]["email"]}, {"_id": 0})
        for every in cursor:
            user.append(every)
        if len(user) == 0:
            raise Exception("No such user whose email : %s" % record[0]['email'])
        user = user[0]
        if "permissions" not in user:
            raise Exception("No extra permissions!")
        if service_id not in user["permissions"]:
            raise Exception("No [%s] service permissions!" % service_id)

    def do_authentication(self, email, password):
        user = self.find_by_email(email)
        if user is None:
            raise Exception("Can't find user of %s!" % email)
        if md5(password) == user["password"]:
            token = uuid()
            self.login_records.insert_one({"email": email, "token": token})
            return token
        raise Exception("Error password!")

    def get_all_users(self):
        cursor = self.data_source.find({}, {"_id": 0})
        users = []
        for every in cursor:
            users.append(every)
        return users

    def remove_user_by_username(self, username):
        self.data_source.delete_many({"username": username})

    def remove_all_users(self):
        self.data_source.delete_many({})


userManager = UserManager(args.mongodb)
limited_prefix = {}


class UserLoginHandler(RequestHandler):
    def post(self):
        req = json.loads(self.request.body.decode(encoding='UTF-8'))
        try:
            token = userManager.do_authentication(req["username"], req["password"])
            self.write({
                "code": 200,
                "token": token
            })
        except Exception as e:
            self.write({
                "code": 400,
                "error": str(e)
            })


# class HttpLinks:
#     links = {}
#     def obtain(self, target):
#         if target not in self.links:
#             links[target] = AsyncHTTPClient()
async_http = AsyncHTTPClient()


class GateHandler(RequestHandler):
    @staticmethod
    def split_path(path):
        return list(filter(lambda x: len(x) != 0, path.split('/')))

    @gen.coroutine
    def multipart_producer(self, boundary, write):
        boundary_bytes = boundary.encode()
        for form_name, many_files in self.request.files.items():
            for file_entity in many_files:
                if "filename" not in file_entity or "body" not in file_entity:
                    continue
                filename = file_entity["filename"]
                filename_bytes = filename.encode()
                formname_bytes = form_name.encode()
                mtype = mimetypes.guess_type(filename)[0] or "application/octet-stream"
                buf = (
                        (b"--%s\r\n" % boundary_bytes)
                        + (
                                b'Content-Disposition: form-data; name="%s"; filename="%s"\r\n'
                                % (formname_bytes, filename_bytes)
                        )
                        + (b"Content-Type: %s\r\n" % mtype.encode())
                        + b"\r\n"
                )
                yield write(buf)
                yield write(file_entity["body"])
                yield write(b"\r\n")

        yield write(b"--%s--\r\n" % (boundary_bytes,))

    async def proxy(self, method="GET"):
        sep = GateHandler.split_path(self.request.path)
        if len(sep) == 0:
            self.write({
                "code": 400,
                "error": "No specific service prefix!"
                })
            return
        prefix = sep[0]

        global limited_prefix
        if prefix in limited_prefix:
            cookie = self.request.headers.get("Cookie")
            token = list(filter(lambda arr: len(arr) == 3 and arr[0] == "UserToken",
                                list(map(lambda s: s.strip().partition("="), cookie.split(";")))))[0][2]
            if token is None:
                token = ""
            if token == "":
                token = self.get_query_argument("id", default="")
            if token == "":
                token = self.request.headers.get("id")
            try:
                userManager.validate(token, limited_prefix.get(prefix).get("service_id"))
            except Exception as e:
                self.write({
                    "code": 401,
                    "error": "Authentication error, %s" % str(e),
                })
                # self.finish()
                return
            if method == "GET":
                response = await async_http.fetch(
                    HTTPRequest("http://%s%s" % (limited_prefix.get(prefix).get("target"), self.request.uri)))
            else:
                if len(self.request.files) != 0:
                    boundary = list(filter(lambda arr: arr[0] == "boundary",
                                           list(map(lambda s: s.strip().partition("="),
                                                    self.request.headers.get("Content-Type").split(";")))))[0][2]
                    producer = partial(self.multipart_producer, boundary)
                    response = await async_http.fetch(
                        "http://%s%s" % (limited_prefix.get(prefix).get("target"), self.request.uri),
                        method="POST",
                        headers={"Content-Type": "multipart/form-data; boundary=%s" % boundary},
                        body_producer=producer)
                else:
                    response = await async_http.fetch(
                        "http://%s%s" % (limited_prefix.get(prefix).get("target"), self.request.uri),
                        method="POST",
                        headers=self.request.headers,
                        body=self.request.body)
            self.write(response.body)
            # self.redirect("http://%s%s" % (limited_prefix.get(prefix).get("target"), self.request.uri), status=status)
        else:
            self.write({"code": 404, "error": "Unknown service!"})

    async def get(self, *arg, **kwargs):
        await self.proxy()

    async def post(self, *arg, **kwargs):
        await self.proxy("POST")


class Service:
    _port = 8000
    _service_name = "general service"
    _version = "v0.1"

    def __init__(self, **kwargs):
        self._port = kwargs['port'] if 'port' in kwargs else self._port
        self._service_name = kwargs['service_name'] if 'service_name' in kwargs else self._service_name
        self._version = kwargs['version'] if 'version' in kwargs else self._version

    def start(self, urls: list):
        logging.info("%s started, listen on %d" % (self._service_name, self._port))
        HTTPServer(Application(urls)).listen(self._port)
        IOLoop.current().start()


def main():
    global limited_prefix
    if os.path.isfile(args.services):
        with open(args.services, 'r+') as fp:
            js = json.loads(fp.read())
            for service_id, service_info in js.items():
                limited_prefix[service_info["prefix"]] = {
                    "service_id": service_id,
                    "target": service_info["target"],
                }
    logging.info("Loading services : " + json.dumps(limited_prefix))
    logging.info("Mongodb services : %s" % args.mongodb)
    urls = [
        (r"/login", UserLoginHandler),
        (r'^/(.*?)$', GateHandler),
    ]
    http = Service(port=int(args.port), service_name="UAS Service", version="v0.1")
    http.start(urls)


if __name__ == '__main__':
    main()
