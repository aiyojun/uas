<template>
  <div ref="layer-1" style="position: relative; width: 100%;">
    <div ref="layer-2" style="display: flex;">
      <div ref="layer-upload" style="position: relative;">
        <div ref="pondEl"></div>
      </div>
      <div ref="layer-fs">
        <div ref="layer-header" style="position: relative;">

          <div class="fm-header" style="display: flex; align-items: center; overflow: hidden;">
            <div class="bg-icon" @click="goHome">
              <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" style="width: 60%;" fill="#fff">
                <path d="M96 480c-9.6 0-19.2-3.2-25.6-12.8-12.8-12.8-9.6-35.2 3.2-44.8l377.6-310.4c35.2-25.6 86.4-25.6 118.4 0l377.6 307.2c12.8 9.6 16 32 3.2 44.8-12.8 12.8-32 16-44.8 3.2L531.2 166.4c-9.6-6.4-28.8-6.4-38.4 0L115.2 473.6c-6.4 6.4-12.8 6.4-19.2 6.4zM816 928H608c-19.2 0-32-12.8-32-32v-150.4c0-22.4-38.4-44.8-67.2-44.8-28.8 0-64 19.2-64 44.8V896c0 19.2-12.8 32-32 32H211.2C163.2 928 128 892.8 128 848V544c0-19.2 12.8-32 32-32s32 12.8 32 32v304c0 9.6 6.4 16 19.2 16H384v-118.4c0-64 67.2-108.8 128-108.8s131.2 44.8 131.2 108.8V864h176c9.6 0 16 0 16-19.2V544c0-19.2 12.8-32 32-32s32 12.8 32 32v304C896 896 864 928 816 928z" p-id="5628"></path>
              </svg>
            </div>
            <div class="bg-icon" @click="goBack">
              <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" style="width: 60%;" fill="#fff">
                <path d="M671.968 912c-12.288 0-24.576-4.672-33.952-14.048L286.048 545.984c-18.752-18.72-18.752-49.12 0-67.872l351.968-352c18.752-18.752 49.12-18.752 67.872 0 18.752 18.72 18.752 49.12 0 67.872l-318.016 318.048 318.016 318.016c18.752 18.752 18.752 49.12 0 67.872C696.544 907.328 684.256 912 671.968 912z" p-id="5474"></path>
              </svg>
            </div>
            <span v-for="(dirItem, dirIndex) in separatedRootPath" :key="dirIndex" class="dir-item" @click="_ => enterDirectoryDirectly(separatedRootPath, dirIndex)">/{{dirItem}}</span>
          </div>

        </div>

        <div ref="layer-mainer" style="position: relative; padding-top: 20px;">

          <div class="top-layer" :style="{gridTemplateColumns: divideColumns, gridGap: `${betweenGap}px`}">
            <div v-for="(fileItem, fileIndex) in widget" :key="fileIndex" class="each-file" :style="{height: `${everyHeight}px`}">
              <div class="file-icon" v-if="fileItem.fileType === 'dir'" :key="'dir'" @click="_ => enterDirectory(fileItem.fileName)">
                <img alt="" :src="PngDir" class="icon"/>
              </div>
              <div class="file-icon" v-else :key="'file'"
                   @mouseenter="fileItem.hover = 1"
                   @mouseleave="fileItem.hover = 0; fileItem.menu = false;">
                <div style="position: absolute; z-index: 1; bottom: 10px; left: 10px; border-radius: 4px; padding: 3px 5px; font-size: 12px; background: linear-gradient(110deg, #8EC5FC, #E0C3FC); color: white;">{{fileItem.fileType}}</div>
                <div v-if="fileItem.hover"
                     style="background: white; height: 20px; width: 20px; position:absolute; top: 0; right: 0; border-radius: 4px; user-select: none;"
                     @mouseenter="fileItem.hover = 2"
                     @mouseleave="fileItem.hover--"
                     @click="fileItem.menu = !fileItem.menu"
                     class="flex-center">
                  <svg viewBox="0 0 1024 1024" style="width: 90%" :fill="fileItem.hover === 2 ? '#333' : '#aaa'">
                    <path d="M192 512m-74.666667 0a74.666667 74.666667 0 1 0 149.333334 0 74.666667 74.666667 0 1 0-149.333334 0Z"></path>
                    <path d="M512 512m-74.666667 0a74.666667 74.666667 0 1 0 149.333334 0 74.666667 74.666667 0 1 0-149.333334 0Z"></path>
                    <path d="M832 512m-74.666667 0a74.666667 74.666667 0 1 0 149.333334 0 74.666667 74.666667 0 1 0-149.333334 0Z"></path>
                  </svg>

                  <div v-if="fileItem.menu" class="menu">
                    <div class="menu-item" @click="_ => downloadFile(fileItem.fileName)">Download</div>
                  </div>
                </div>

                <img v-if="['rar','zip','tar','gz','xz'].indexOf(fileItem.fileType) > -1" alt="" :src="PngCompress" class="icon"/>
                <img v-else-if="fileItem.fileType === 'rar'" alt="" :src="PngCompress" class="icon"/>
                <img v-else-if="['mp3','mp4','avi','rmvb','flv'].indexOf(fileItem.fileType) > -1" alt="" :src="PngMedia" class="icon"/>
                <img v-else-if="fileItem.fileType === 'txt'" alt="" :src="PngTxt" class="icon"/>
                <img v-else-if="fileItem.fileType === 'js'" alt="" :src="PngJs" class="icon"/>
                <img v-else-if="fileItem.fileType === 'md'" alt="" :src="PngMd" class="icon"/>
                <img v-else-if="fileItem.fileType === 'json'" alt="" :src="PngJson" class="icon"/>
                <img v-else-if="fileItem.fileType === 'html'" alt="" :src="PngHtml" class="icon"/>
                <img v-else-if="fileItem.fileType === 'css'" alt="" :src="PngCss" class="icon"/>
                <img v-else-if="fileItem.fileType === 'svg'" alt="" :src="trimPath(`${prefix}/${rootPath}${fileItem.fileName}?id=${token}`, false)" class="random-icon"/>
                <img v-else-if="fileItem.fileType === 'png'" alt="" :src="trimPath(`${prefix}/${rootPath}${fileItem.fileName}?id=${token}`, false)" class="random-icon"/>
                <img v-else-if="fileItem.fileType === 'jpg'" alt="" :src="trimPath(`${prefix}/${rootPath}${fileItem.fileName}?id=${token}`, false)" class="random-icon"/>
                <img v-else-if="fileItem.fileType === 'jpeg'" alt="" :src="trimPath(`${prefix}/${rootPath}${fileItem.fileName}?id=${token}`, false)" class="random-icon"/>
                <img v-else alt="" :src="PngAll" class="icon"/>
              </div>

              <div class="file-name" :key="'icon'"><span class="file-font">{{fileItem.fileName}}</span></div>
            </div>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>

import axios from "axios";
import "filepond/dist/filepond.css"
import * as FilePond from 'filepond/dist/filepond';

import PngDir from "@/assets/directory.png"
import PngTxt from "@/assets/ali-file-txt.png"
import PngAll from "@/assets/ali-file-code.png"
import PngCompress from "@/assets/rar.png"
import PngHtml from "@/assets/ali-file-html.png"
import PngJs from "@/assets/ali-file-js.png"
import PngXml from "@/assets/ali-file-xml.png"
import PngJson from "@/assets/ali-file-json.png"
import PngMd from "@/assets/ali-file-markdown.png"
import PngCss from "@/assets/ali-file-css.png"
import PngMedia from "@/assets/ali-file-video.png"

function trimPath(path, isDir=true) {
  path = isDir ? `${path.split('/').filter(i => i.length !== 0).join('/')}/` : `${path.split('/').filter(i => i.length !== 0).join('/')}`
  if (path.indexOf('http') > -1) {
    path = path.split(':/').join('://')
  } else if (path[0] !== '/') {
    path = `/${path}`
  }
  return path
}

class Communicator {
  list(token, path = '/', prefix = '/fs') {
    console.info(`Communicator ${trimPath(`${prefix}${path}`)}`)
    console.info(`token: ${token}`)
    return axios.get(trimPath(`${prefix}${path}`), {
      params: {id: token},
      headers: {
        'Content-Type': 'text/html; charset=utf-8',
      }
    })
  }
}

export default {
  name: "FileManager",
  props: {
    prefix: { type: String, default: '/fs' },
    // column: { type: Number, default: 10 },
  },
  computed: {
    separatedRootPath() {
      return this.rootPath.split('/').filter(i => i.length !== 0)
    },
    divideColumns() {
      const arr = []
      for (let i = 0; i < this.column; i++)
        arr.push(`${this.everyWidth}px`)
      return `${arr.join(' ')}`
    },
  },
  data() {
    return {
      PngDir, PngAll, PngTxt, PngCompress, PngHtml, PngJs, PngXml, PngJson, PngMd, PngCss, PngMedia,
      communicator: new Communicator(),
      rootPath: '/',
      widget: [ ],
      everyHeight: 120,
      everyWidth: 120,
      betweenGap: 10,
      column: 12,
      token: '',
    }
  },

  created() {
    this.token = this.findUsefulToken()
    if (this.token === null || this.token === undefined) {
      this.token = ''
    }
    window.addEventListener("load"  , this.layout$ui)
    window.addEventListener("resize", this.layout$ui)
    this.communicator.list(this.token, this.rootPath, this.prefix).then(response => this.parse(response.data))
  },
  mounted() {
    const self = this
    FilePond.create(this.$refs.pondEl, {
      server: trimPath(`${self.prefix}${self.rootPath}`),
      allowMultiple: true,
      name: 'filepond',
    })
    FilePond.setOptions({
      onprocessfile: function () {
        self.communicator.list(this.token, self.rootPath, self.prefix).then(response => self.parse(response.data))
      }
    })
  },
  destroyed() {
    FilePond.destroy(this.$refs.pondEl)
  },
  methods: {
    findUsefulToken() {
      const permanent = {}
      document.cookie
          .split(';')
          .filter(i => i.indexOf('=') > -1)
          .map(i => i.split('='))
          .filter(i => i.length === 2)
          .forEach(i => permanent[i[0].trim()] = i[1].trim())
      if (!permanent.hasOwnProperty('UserToken'))
        return null
      return permanent.UserToken
    },
    layout$ui() {
      const W = this.$refs["layer-1"].offsetWidth
      let fsw = W
      if (W <= 800 || window.screen.width <= 800) {
        this.$refs["layer-2"].style.flexDirection = 'column'
        this.$refs["layer-upload"].style.width = '100%'
        this.$refs["layer-fs"].style.width = '100%'
        this.$refs["layer-header"].style.paddingLeft = '0'
        this.$refs["layer-header"].style.paddingRight = '0'
        this.$refs["layer-header"].style.marginTop = '10px'
        this.betweenGap = 5
        if (W < 400) {
          this.column = 4
        } else {
          this.column = 5
        }
      } else {
        const pondWidth = 400
        fsw -= pondWidth
        this.$refs["layer-2"].style.flexDirection = 'row'
        this.$refs["layer-upload"].style.width = `${pondWidth}px`
        this.$refs["layer-fs"].style.width = `calc(100% - ${pondWidth}px)`
        this.$refs["layer-header"].style.paddingLeft = '20px'
        this.$refs["layer-header"].style.paddingRight = '20px'
        this.$refs["layer-header"].style.marginTop = '0'
        this.betweenGap = 10
        if (W < 960) {
          this.betweenGap = 5
          this.column = 5
        } else if (W < 1120) {
          this.column = 6
        } else if (W < 1280) {
          this.column = 8
        } else if (W < 1520) {
          this.column = 10
        } else {
          this.column = 12
        }
      }
      this.everyWidth  = Math.round(Math.abs(fsw - (this.column - 1) * this.betweenGap) / this.column)
      this.everyHeight = Math.round(Math.abs(fsw - (this.column - 1) * this.betweenGap) / this.column)
    },
    trimPath(path, isDir=true) {
      return trimPath(path, isDir)
    },
    downloadFile(filename) {
      this.linkDownload(`${this.prefix}${this.rootPath}${filename}`, filename)
    },
    enterDirectory(d) {
      this.clearWidget()
      this.rootPath = `${this.rootPath}${d}/`
      FilePond.setOptions({server: trimPath(`${this.prefix}${this.rootPath}`)})
      this.communicator.list(this.token, this.rootPath, this.prefix).then(response => this.parse(response.data))
    },
    enterDirectoryDirectly(vec, index) {
      const paths = []
      for (let i = 0; i < index + 1; i++) {
        paths.push(vec[i])
      }
      this.clearWidget()
      this.rootPath = `/${paths.join('/')}`
      if (this.rootPath[this.rootPath.length - 1] !== '/') this.rootPath += '/'
      FilePond.setOptions({server: trimPath(`${this.prefix}${this.rootPath}`)})
      this.communicator.list(this.token, this.rootPath, this.prefix).then(response => this.parse(response.data))
    },
    goBack() {
      if (this.rootPath === '/') return
      let paths = this.rootPath.split('/')
      paths = paths.filter(i => i.length !== 0)
      paths.pop()
      this.clearWidget()
      this.rootPath = paths.length > 0 ? `/${paths.join('/')}/` : '/'
      FilePond.setOptions({server: trimPath(`${this.prefix}${this.rootPath}`)})
      this.communicator.list(this.token, this.rootPath, this.prefix).then(response => this.parse(response.data))
    },
    goHome() {
      this.clearWidget()
      this.rootPath = `/`
      FilePond.setOptions({server: trimPath(`${this.prefix}${this.rootPath}`)})
      this.communicator.list(this.token, this.rootPath, this.prefix).then(response => this.parse(response.data))
    },
    clearWidget() {
      this.widget.splice(0, this.widget.length)
    },
    parse(s) {
      const doc = new DOMParser().parseFromString(s, "text/html")
      const items = doc.getElementsByTagName('a')
      this.clearWidget()
      let arr = []
      for (let i = 0; i < items.length; i++) {
        const link = items[i]
        const filename = link.innerText.split('/').filter(j => j.length !== 0).pop()
        const dotIndex = filename.indexOf('.')
        let filetype = (dotIndex > 0 ? filename.split('.').pop() : 'file').toLowerCase()
        if (filetype.length > 6) {
          filetype = 'file'
        }
        if (link.innerText[link.innerText.length - 1] === '/') {
          arr.push({ fileType: 'dir', fileName: filename, hover: 0, menu: false })
        } else if (dotIndex > 0) {
          arr.push({ fileType: filetype, fileName: filename, hover: 0, menu: false })
        } else if (dotIndex === -1) {
          arr.push({ fileType: filetype, fileName: filename, hover: 0, menu: false })
        }
      }
      arr = this.sortByFileTypeAndName(arr)
      arr.forEach(e => {this.widget.push(e)})
      console.info(`widget:`)
      this.widget.forEach(e => {
        console.info(`  ${e.fileName}`)
      })
    },
    sortByName(arr) {
      arr.sort((o0,o1)=>{return o0.fileName.localeCompare(o1.fileName)})
      return arr
    },
    sortByFileTypeAndName(arr) {
      let dirs = []
      let files = []
      for (let i = 0; i < arr.length; i++) {
        if (arr[i].fileType === 'dir') {
          dirs.push(arr[i])
        } else {
          files.push(arr[i])
        }
      }
      dirs = this.sortByName(dirs)
      files = this.sortByName(files)
      return [...dirs, ...files]
    },
    linkDownload(url, filename) {
      const el = document.createElement('a');
      el.style.display = 'none';
      el.setAttribute('target', '_blank');
      filename && el.setAttribute('download', filename)
      el.href = url
      document.body.appendChild(el)
      el.click()
      document.body.removeChild(el)
    }
  },
}
</script>

<style scoped>

.fm-header {
  height: 42px;
  padding: 0 3px;
  background: linear-gradient(110deg, #8EC5FC, #E0C3FC);
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(23,24,25,0.3);
}

.bg-fm {
  position: relative;
}

.top-layer {
  /*padding-top: 50px;*/
  /*width: 600px;*/
  width: 100%;
  display: grid;
  /*grid-gap: 10px;*/
}

.each-file {
  /*margin: 2px;*/
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  /*height: 120px;*/
  border-radius: 8px;
}

.each-file:hover {
  background-color: rgba(200,200,200,.3);
}

.file-icon {
  position: relative;
  width: 90%;
  height: calc(90% - 28px);
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}

.file-name {
  width: 100%;
  height: 28px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.file-font {
  width: 90%;
  font-size: 14px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  text-align: center;
}

.bg-icon {
  width: 36px;
  height: 36px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  border-radius: 8px;
  margin-right: 5px;
}

.bg-icon:hover {
  background: rgba(56,57,58,0.1);
}

.flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

.icon {
  max-height: 90%;
  max-width: 90%;
}

.random-icon {
  max-height: 60%;
  max-width: 60%;
}

.dir-item {
  display: inline-block;
  padding: 4px 5px;
  border-radius: 4px;
  color: white;
  font-size: 16px;
  margin-right: 3px;
  cursor: pointer;
  white-space: nowrap;
}

.dir-item:hover {
  background: rgba(56,57,58,0.1);
}

.menu {
  position: absolute;
  z-index: 2;
  top: 25px;
  right: 0;
  background: white;
  padding: 0 5px;
  border-radius: 4px;
  box-shadow: 0 1px 3px rgba(23,24,25,0.3);
}

.menu-item {
  min-width: 120px;
  text-align: left;
  border-radius: 4px;
  margin: 5px 0;
  padding: 3px 10px;
}

.menu-item:hover {
  background: #eee;
}

</style>
