import os
import logging
import argparse
from urllib.parse import unquote

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer


def arg_help():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', default=8000, help='port of service')
    parser.add_argument('-D', '--directory', default=".", help='directory of static files')
    parser.add_argument('-f', '--prefix', default="", help='prefix of url')
    return parser.parse_args()


logging.basicConfig(
    format='%(asctime)s [%(threadName)s] [%(name)s] [%(levelname)s] %(filename)s[line:%(lineno)d] %(message)s',
    level=logging.INFO
)
args = arg_help()
static_path = args.directory
service_prefix = args.prefix


class FileManagerHandler(RequestHandler):
    @staticmethod
    def trim(path):
        path = "/".join(list(filter(lambda s: len(s) != 0, path.split('/'))))
        return path

    @staticmethod
    def real_file_name(path):
        arr = list(filter(lambda s: len(s) != 0, path.split('/')))
        return arr[-1]

    @staticmethod
    def list_dir(path):
        global static_path
        real_path = static_path + "/" + FileManagerHandler.trim(path)
        if real_path[-1] != "/":
            real_path += "/"
        files = os.listdir(real_path)
        ul = ""
        html = '''<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>Directory listing for ${PATH}$</title></head><body><h1>Directory listing for ${PATH}$</h1><hr><ul>${CONTENT}$</ul><hr></body></html>'''
        for file in files:
            if os.path.isdir(real_path + file):
                real_dir = file + "/"
                ul += "<li><a href=\"%s\">%s</a></li>" % (real_dir, real_dir)
            else:
                ul += "<li><a href=\"%s\">%s</a></li>" % (file, file)
        html = html.replace("${PATH}$", real_path.replace(static_path, ""))
        html = html.replace("${CONTENT}$", ul)
        return html

    @staticmethod
    def get_file_path(path):
        global static_path
        return static_path + "/" + FileManagerHandler.trim(path)

    def get(self, *arg, **kwargs):
        relative_path = unquote(self.request.path)
        global service_prefix
        if relative_path.find(service_prefix) >= 0:
            relative_path = relative_path[len(service_prefix):]
        if len(relative_path) == 0:
            relative_path = "/"
        if relative_path[-1] == "/":
            self.write(FileManagerHandler.list_dir(relative_path))
        else:
            real_file_path = FileManagerHandler.get_file_path(relative_path)
            # bytes_n = os.stat(real_file_path).st_size
            bytes_n = 0
            self.set_header("Content-Description", "File Transfer")
            self.set_header("Content-Type", "application/octet-stream")
            self.set_header("Content-Disposition", FileManagerHandler.real_file_name(real_file_path).encode("utf-8"))
            self.set_header("Content-Transfer-Encoding", "binary")
            with open(real_file_path, 'rb+') as fp:
                chunk = fp.read(16 * 1024)
                while chunk:
                    bytes_n += len(chunk)
                    self.write(chunk)
                    chunk = fp.read(16 * 1024)
            self.set_header("Content-Length", str(bytes_n))
        self.finish()

    def post(self, *arg, **kwargs):
        relative_path = unquote(self.request.path)
        global service_prefix
        if relative_path.find(service_prefix) >= 0:
            relative_path = relative_path[len(service_prefix):]
        # form_keys = list(self.request.files.keys())
        # for form_key in form_keys:
        #     form = self.request.files.get(form_key)
        multi_files = self.request.files.get("filepond")
        if not multi_files:
            self.write({"code": 500})
            return
        for file in multi_files:
            filename = file["filename"]
            real_dir = FileManagerHandler.trim(static_path + "/" + relative_path) + "/"
            if not os.path.exists(real_dir):
                os.mkdir(real_dir)
            real_file_path = FileManagerHandler.trim(real_dir + "/" + filename)
            if os.path.exists(real_file_path):
                os.remove(real_file_path)
            with open(real_file_path, 'wb+') as fp:
                fp.write(file["body"])
        self.write({"code": 200})
        self.finish()

    def delete(self, *arg, **kwargs):
        relative_path = unquote(self.request.path)


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
        logging.info("Access prefix    : %s" % service_prefix)
        logging.info("Access directory : %s" % args.directory)
        HTTPServer(Application(urls)).listen(self._port)
        IOLoop.current().start()


def main():
    urls = [
        (r'^/(.*?)$', FileManagerHandler),
    ]
    http = Service(port=int(args.port), service_name="FTP Service", version="v0.1")
    http.start(urls)


if __name__ == '__main__':
    main()
