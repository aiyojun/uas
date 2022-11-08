<template>
  <div style="position: relative; width: 100%; height: 100%; background-color: #fff; overflow-y: auto; overflow-x: auto;">
    <div style="margin: 10px;">
      <span>Recent access</span>

      <table class="global-table">
        <tr class="table-line">
          <th class="table-header">Remote ip</th>
          <th class="table-header">Access uri</th>
          <th class="table-header">Time</th>
          <th class="table-header">OS</th>
          <th class="table-header">Browser</th>
          <th class="table-header">
            <div style="display: flex; align-items: center;">
              <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" width="24" height="24">
                <path d="M512 608c-105.888 0-192-86.112-192-192s86.112-192 192-192 192 86.112 192 192S617.888 608 512 608zM512 288c-70.592 0-128 57.408-128 128s57.408 128 128 128c70.592 0 128-57.408 128-128S582.592 288 512 288z"></path>
                <path d="M512 960c-7.936 0-15.904-2.944-22.08-8.832-12.768-12.224-13.248-32.48-1.056-45.248C575.392 815.2 800 550.336 800 416c0-158.784-129.184-288-288-288-158.784 0-288 129.216-288 288 0 75.616 72.544 206.08 204.256 367.424 11.2 13.728 9.152 33.888-4.544 45.024-13.696 11.168-33.888 9.152-45.024-4.544C233.568 646.176 160 508.928 160 416 160 221.92 317.92 64 512 64s352 157.92 352 352c0 187.36-315.424 520.032-328.832 534.08C528.864 956.672 520.448 960 512 960z"></path>
              </svg>
              <div>
                Geo
              </div>
            </div>
          </th>
        </tr>
        <tr v-for="(remoteLink, lineNumber) in views" class="table-line">
          <td class="table-block" style="width: 180px;" :style="{backgroundColor: (lineNumber + 1) % 2 === 1 ? `rgba(0,0,0,0)` : `rgba(0,0,0,0.03)`}">{{remoteLink['remote_address'].split(':')[0]}}</td>
          <td class="table-block" style="width: 180px;" :style="{backgroundColor: (lineNumber + 1) % 2 === 1 ? `rgba(0,0,0,0)` : `rgba(0,0,0,0.03)`}">{{remoteLink['access_uri']}}</td>
          <td class="table-block" :style="{backgroundColor: (lineNumber + 1) % 2 === 1 ? `rgba(0,0,0,0)` : `rgba(0,0,0,0.03)`}">{{new Date(remoteLink['access_time']).Format('yyyy-MM-dd hh:mm:ss')}}</td>
          <td class="table-block" :style="{backgroundColor: (lineNumber + 1) % 2 === 1 ? `rgba(0,0,0,0)` : `rgba(0,0,0,0.03)`}">{{remoteLink.hasOwnProperty('extra') ? `${hideNull(remoteLink['extra']['os_family'])} ${hideNull(remoteLink['extra']['os_version'])}` : ''}}</td>
          <td class="table-block" :style="{backgroundColor: (lineNumber + 1) % 2 === 1 ? `rgba(0,0,0,0)` : `rgba(0,0,0,0.03)`}">{{remoteLink.hasOwnProperty('extra') ? `${hideNull(remoteLink['extra']['browser_family'])} ${hideNull(remoteLink['extra']['browser_version'])}` : ''}}</td>
          <td class="table-block" :style="{backgroundColor: (lineNumber + 1) % 2 === 1 ? `rgba(0,0,0,0)` : `rgba(0,0,0,0.03)`}">{{ipGeo.hasOwnProperty(remoteLink['remote_address'].split(':')[0]) ? buildGeo(ipGeo[remoteLink['remote_address'].split(':')[0]]) : ''}}</td>
        </tr>
      </table>
    </div>

  </div>
</template>

<script>

import axios from "axios";

Date.prototype.Format = function (fmt) {
  const o = {
    "M+": this.getMonth() + 1,
    "d+": this.getDate(),
    "h+": this.getHours(),
    "m+": this.getMinutes(),
    "s+": this.getSeconds(),
    "q+": Math.floor((this.getMonth() + 3) / 3),
    "S": this.getMilliseconds()
  };
  if (/(y+)/.test(fmt))
    fmt = fmt.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length));
  for (let k in o)
    if (new RegExp("(" + k + ")").test(fmt))
      fmt = fmt.replace(RegExp.$1, (RegExp.$1.length === 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
  return fmt;
}

export default {
  name: "ServerDashboard",
  data() {
    return {
      remoteLinks: [],
      timeSortAsc: true,
      views: [],
      ipHash: {},
      ipGeo: {},
    }
  },
  mounted() {
    this.remoteLinks.splice(0, this.remoteLinks.length);
    const resp = {data:{"log": [{"remote_address": "40.77.167.104:40768", "access_uri": "/cansijdbcasujhdbcahsbdcbasjdbhasbfcd/robots.txt", "access_by_host": "djun.xyz", "access_time": 1661717286076, "extra": {"browser_family": "bingbot", "browser_version": "2.0", "os_family": "Other", "os_version": "", "device_family": "Spider", "device_brand": "Spider", "device_model": "Desktop"}}, {"remote_address": "40.77.167.104:35264", "access_uri": "/robots.txt", "access_by_host": "djun.xyz", "access_time": 1661710287211, "extra": {"browser_family": "bingbot", "browser_version": "2.0", "os_family": "Other", "os_version": "", "device_family": "Spider", "device_brand": "Spider", "device_model": "Desktop"}}, {"remote_address": "45.140.185.39:58530", "access_uri": "/", "access_by_host": "www.djun.xyz", "access_time": 1661701555741, "extra": {"browser_family": "Firefox", "browser_version": "83.0", "os_family": "Linux", "os_version": "", "device_family": "Other", "device_brand": null, "device_model": null}}, {"remote_address": "45.140.185.39:58352", "access_uri": "/.env", "access_by_host": "www.djun.xyz", "access_time": 1661701554658, "extra": {"browser_family": "Firefox", "browser_version": "83.0", "os_family": "Linux", "os_version": "", "device_family": "Other", "device_brand": null, "device_model": null}}, {"remote_address": "36.32.2.202:38904", "access_uri": "/1jlbdmb", "access_by_host": "djun.xyz", "access_time": 1661692621636, "extra": {"browser_family": "IE", "browser_version": "6.0", "os_family": "Windows", "os_version": "XP", "device_family": "Other", "device_brand": null, "device_model": null}}, {"remote_address": "123.144.26.230:38688", "access_uri": "/index.html", "access_by_host": "djun.xyz", "access_time": 1661692619622, "extra": {"browser_family": "Chrome Mobile", "browser_version": "55.0.2883", "os_family": "Android", "os_version": "6.0", "device_family": "Nexus 5", "device_brand": "LG", "device_model": "Nexus 5"}}, {"remote_address": "123.144.26.230:38688", "access_uri": "/", "access_by_host": "djun.xyz", "access_time": 1661692619302, "extra": {"browser_family": "Chrome Mobile", "browser_version": "55.0.2883", "os_family": "Android", "os_version": "6.0", "device_family": "Nexus 5", "device_brand": "LG", "device_model": "Nexus 5"}}, {"remote_address": "124.133.209.188:37932", "access_uri": "/favicon.ico", "access_by_host": "djun.xyz", "access_time": 1661692612855, "extra": {"browser_family": "Chrome", "browser_version": "68.0.3440", "os_family": "Mac OS X", "os_version": "10.13.6", "device_family": "Mac", "device_brand": "Apple", "device_model": "Mac"}}, {"remote_address": "111.224.235.165:37284", "access_uri": "/1jlbdmb", "access_by_host": "djun.xyz", "access_time": 1661692609811, "extra": {"browser_family": "Mobile Safari", "browser_version": "9.0", "os_family": "iOS", "os_version": "9.1", "device_family": "iPhone", "device_brand": "Apple", "device_model": "iPhone"}}, {"remote_address": "124.235.138.48:36732", "access_uri": "/index.html", "access_by_host": "djun.xyz", "access_time": 1661692600489, "extra": {"browser_family": "Chrome Mobile", "browser_version": "55.0.2883", "os_family": "Android", "os_version": "6.0", "device_family": "Nexus 5", "device_brand": "LG", "device_model": "Nexus 5"}}, {"remote_address": "124.235.138.48:36732", "access_uri": "/", "access_by_host": "djun.xyz", "access_time": 1661692599570, "extra": {"browser_family": "Chrome Mobile", "browser_version": "55.0.2883", "os_family": "Android", "os_version": "6.0", "device_family": "Nexus 5", "device_brand": "LG", "device_model": "Nexus 5"}}, {"remote_address": "124.117.193.39:36524", "access_uri": "/favicon.ico", "access_by_host": "djun.xyz", "access_time": 1661692598588, "extra": {"browser_family": "Chrome Mobile", "browser_version": "55.0.2883", "os_family": "Android", "os_version": "6.0", "device_family": "Nexus 5", "device_brand": "LG", "device_model": "Nexus 5"}}, {"remote_address": "123.245.25.186:42466", "access_uri": "/index.html", "access_by_host": "djun.xyz", "access_time": 1661692598184, "extra": {"browser_family": "Edge", "browser_version": "17.17134", "os_family": "Windows", "os_version": "10", "device_family": "Other", "device_brand": null, "device_model": null}}, {"remote_address": "123.245.25.186:42466", "access_uri": "/", "access_by_host": "djun.xyz", "access_time": 1661692597917, "extra": {"browser_family": "Edge", "browser_version": "17.17134", "os_family": "Windows", "os_version": "10", "device_family": "Other", "device_brand": null, "device_model": null}}, {"remote_address": "66.249.68.66:37918", "access_uri": "/index.html", "access_by_host": "www.djun.xyz", "access_time": 1661682071978, "extra": {"browser_family": "Googlebot", "browser_version": "2.1", "os_family": "Android", "os_version": "6.0.1", "device_family": "Spider", "device_brand": "Spider", "device_model": "Smartphone"}}, {"remote_address": "66.249.68.70:35378", "access_uri": "/", "access_by_host": "www.djun.xyz", "access_time": 1661682071307, "extra": {"browser_family": "Googlebot", "browser_version": "2.1", "os_family": "Android", "os_version": "6.0.1", "device_family": "Spider", "device_brand": "Spider", "device_model": "Smartphone"}}, {"remote_address": "66.249.68.69:58405", "access_uri": "/robots.txt", "access_by_host": "www.djun.xyz", "access_time": 1661682069727, "extra": {"browser_family": "Googlebot", "browser_version": "2.1", "os_family": "Other", "os_version": "", "device_family": "Spider", "device_brand": "Spider", "device_model": "Desktop"}}, {"remote_address": "8.45.47.67:22768", "access_uri": "/favicon.ico", "access_by_host": "djun.xyz", "access_time": 1661678061030, "extra": {"browser_family": "Chrome", "browser_version": "96.0.4664", "os_family": "Mac OS X", "os_version": "10.15.7", "device_family": "Mac", "device_brand": "Apple", "device_model": "Mac"}}, {"remote_address": "8.45.47.67:22768", "access_uri": "/index.html", "access_by_host": "djun.xyz", "access_time": 1661678059881, "extra": {"browser_family": "Chrome", "browser_version": "96.0.4664", "os_family": "Mac OS X", "os_version": "10.15.7", "device_family": "Mac", "device_brand": "Apple", "device_model": "Mac"}}, {"remote_address": "8.45.47.67:22768", "access_uri": "/", "access_by_host": "djun.xyz", "access_time": 1661678059473, "extra": {"browser_family": "Chrome", "browser_version": "96.0.4664", "os_family": "Mac OS X", "os_version": "10.15.7", "device_family": "Mac", "device_brand": "Apple", "device_model": "Mac"}}]}};
    // axios
    //     .get(`log/caddy?line_number=${500}`)
    //     .then(resp => {
          for (let remote_address in resp.data.log) {
            const remoteLink = resp.data.log[remote_address]
            try {
              this.remoteLinks.push(remoteLink)
              if (remoteLink['geo'] !== undefined && remoteLink['geo'] !== null) {
                this.$set(this.ipGeo, remoteLink['remote_address'].split(':')[0], remoteLink['geo'])
              }
              this.views.push(remoteLink);
            } catch (e) {

            }
          }
        // })
        // .catch(err => {
        //
        // })
  },
  methods: {
    hideNull(v) {return (v === null || v === undefined) ? '' : v;},
    sortByTime(asc=true) {
      asc
          ? this.views.sort((o0, o1) => o0['access_time'] < o1['access_time'] ? 1 : -1)
          : this.views.sort((o0, o1) => o0['access_time'] > o1['access_time'] ? 1 : -1)
      ;
      this.timeSortAsc = asc;
    },
    showOnly(k, v) {
      this.$set(this, 'ipHash', {});
      this.views.splice(0, this.remoteLinks.length);
      for (let i = 0; i < this.remoteLinks.length; i++) {
        const remoteLink = this.remoteLinks[i];
        if (k === undefined) {
          this.views.push(remoteLink);
        } else if (k === 'ip' && v === remoteLink['remote_address'].split(':')[0]) {
          this.views.push(remoteLink);
        } else if (v === remoteLink[k]) {
          this.views.push(remoteLink);
        }
      }
    },
    async __getGeo(ip) {
      const self = this;
      await axios
          .get(`/ip/geo?ip=${ip}`)
          .then(resp => {
            self.$set(this.ipGeo, ip, resp.data);
          })
    },
    async getGeo(ip) {
      if (this.ipGeo.hasOwnProperty(ip) && this.ipGeo[ip] !== undefined) {
        return this.ipGeo[ip];
      } else {
        await this.__getGeo(ip);
        return this.ipGeo[ip];
      }
    },
    buildUnknown(s) {return s === '' ? 'unknown' : s;},
    buildGeo(geo) {return `${this.buildUnknown(geo['city'])}-${this.buildUnknown(geo['province'])}-${this.buildUnknown(geo['country'])} ${this.buildUnknown(geo['isp'])}`},
  }
}
</script>

<style scoped>

.global-table {
  border-spacing: 0;
}

.table-header {
  height:48px;
  /*background: linear-gradient(0deg, rgba(230,230,230,1.0), rgba(250,250,250,1.0), rgba(230,230,230,1.0));*/
  /*max-width: 300px;*/
  /*font-size: 16px;*/
  font-weight: normal;
  text-align: left;
}

.table-block {
  height: 48px;
  text-align: left;
  /*max-width: 300px;*/

  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;

  border-top: 1px solid #ddd;
  color: #707070;
}

.table-line {

}

</style>