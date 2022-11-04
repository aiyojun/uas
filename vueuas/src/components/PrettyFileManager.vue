<template>
  <div ref="topLayer" style="width: 100%; position: relative;">
    <div style="width: calc(100% - 20px); padding: 10px;">
<!--    <div style="width: calc(100% - 4px - 32px); border: 2px solid #555; height: 32px; border-radius: 32px; padding-left: 16px; padding-right: 16px; display: flex; align-items: center;">-->
      <div style="overflow-x: hidden; width: calc(100% - 32px); height: 32px; border-radius: 32px; padding-left: 16px; padding-right: 16px; color: #333; box-shadow: 0 1px 4px rgba(23,24,25,0.2); display: flex; align-items: center; justify-content: flex-start;">
        <div class="icon-outer central" style="min-width: 28px;">
          <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" style="width: 70%;" fill="#333">
            <path d="M96 480c-9.6 0-19.2-3.2-25.6-12.8-12.8-12.8-9.6-35.2 3.2-44.8l377.6-310.4c35.2-25.6 86.4-25.6 118.4 0l377.6 307.2c12.8 9.6 16 32 3.2 44.8-12.8 12.8-32 16-44.8 3.2L531.2 166.4c-9.6-6.4-28.8-6.4-38.4 0L115.2 473.6c-6.4 6.4-12.8 6.4-19.2 6.4zM816 928H608c-19.2 0-32-12.8-32-32v-150.4c0-22.4-38.4-44.8-67.2-44.8-28.8 0-64 19.2-64 44.8V896c0 19.2-12.8 32-32 32H211.2C163.2 928 128 892.8 128 848V544c0-19.2 12.8-32 32-32s32 12.8 32 32v304c0 9.6 6.4 16 19.2 16H384v-118.4c0-64 67.2-108.8 128-108.8s131.2 44.8 131.2 108.8V864h176c9.6 0 16 0 16-19.2V544c0-19.2 12.8-32 32-32s32 12.8 32 32v304C896 896 864 928 816 928z" p-id="5628"></path>
          </svg>
        </div>
        <div v-for="(dirItem, dirIndex) in separatedRootPath" :key="`dir-${dirIndex}`" style="display: flex; align-items: center; margin-left: 3px;">
          <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" style="width: 16px; height: 16px; margin-right: 3px; display: inline-block;" fill="#bcd4f6" stroke-linecap="round" stroke-linejoin="miter">
            <path d="M817.088 484.96l-512-323.744C295.232 154.976 282.752 154.592 272.576 160.224 262.336 165.856 256 176.608 256 188.256l0 647.328c0 11.648 6.336 22.4 16.576 28.032 4.8 2.656 10.112 3.968 15.424 3.968 5.952 0 11.904-1.664 17.088-4.928l512-323.616C826.368 533.184 832 522.976 832 512 832 501.024 826.368 490.816 817.088 484.96z"></path>
          </svg>

          <div class="directory-level">

            {{dirItem}}
          </div>
        </div>

      </div>
    </div>

    <div style="width: 100%; min-height: 80px; position: relative;">
      <div class="central" style="position: absolute; width: 32px; height: 32px; bottom: 10px; right: 10px; border-radius: 32px; box-shadow: 1px 1px 4px rgba(23,24,25,0.2); cursor: pointer;">
        <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" style="width: 70%;" fill="#888">
          <path d="M213.333333 426.666667c-25.6 0-42.666667-17.066667-42.666667-42.666667 0-166.4 132.266667-298.666667 298.666667-298.666667 128 0 243.2 85.333333 285.866667 209.066667C759.466667 315.733333 750.933333 341.333333 725.333333 345.6c-21.333333 8.533333-46.933333-4.266667-55.466667-25.6C644.266667 230.4 563.2 170.666667 469.333333 170.666667 349.866667 170.666667 256 264.533333 256 384 256 409.6 238.933333 426.666667 213.333333 426.666667z" p-id="3639"></path><path d="M768 768c-25.6 0-42.666667-17.066667-42.666667-42.666667s17.066667-42.666667 42.666667-42.666667c93.866667 0 170.666667-76.8 170.666667-170.666667s-76.8-170.666667-170.666667-170.666667c-12.8 0-29.866667 0-42.666667 4.266667-21.333333 4.266667-46.933333-8.533333-51.2-29.866667s8.533333-46.933333 29.866667-51.2C725.333333 260.266667 746.666667 256 768 256c140.8 0 256 115.2 256 256S908.8 768 768 768z" p-id="3640"></path><path d="M341.333333 768 213.333333 768c-25.6 0-42.666667-17.066667-42.666667-42.666667s17.066667-42.666667 42.666667-42.666667l128 0c25.6 0 42.666667 17.066667 42.666667 42.666667S366.933333 768 341.333333 768z" p-id="3641"></path><path d="M768 768l-85.333333 0c-25.6 0-42.666667-17.066667-42.666667-42.666667s17.066667-42.666667 42.666667-42.666667l85.333333 0c25.6 0 42.666667 17.066667 42.666667 42.666667S793.6 768 768 768z" p-id="3642"></path><path d="M213.333333 768c-119.466667 0-213.333333-93.866667-213.333333-213.333333s93.866667-213.333333 213.333333-213.333333c25.6 0 42.666667 17.066667 42.666667 42.666667s-17.066667 42.666667-42.666667 42.666667c-72.533333 0-128 55.466667-128 128s55.466667 128 128 128c25.6 0 42.666667 17.066667 42.666667 42.666667S238.933333 768 213.333333 768z" p-id="3643"></path><path d="M512 938.666667c-25.6 0-42.666667-17.066667-42.666667-42.666667L469.333333 469.333333c0-25.6 17.066667-42.666667 42.666667-42.666667s42.666667 17.066667 42.666667 42.666667l0 426.666667C554.666667 921.6 537.6 938.666667 512 938.666667z" p-id="3644"></path><path d="M384 640c-12.8 0-21.333333-4.266667-29.866667-12.8-17.066667-17.066667-17.066667-42.666667 0-59.733333l128-128c17.066667-17.066667 42.666667-17.066667 59.733333 0s17.066667 42.666667 0 59.733333l-128 128C405.333333 635.733333 396.8 640 384 640z" p-id="3645"></path><path d="M640 640c-12.8 0-21.333333-4.266667-29.866667-12.8l-128-128c-17.066667-17.066667-17.066667-42.666667 0-59.733333s42.666667-17.066667 59.733333 0l128 128c17.066667 17.066667 17.066667 42.666667 0 59.733333C661.333333 635.733333 652.8 640 640 640z"></path>
        </svg>
      </div>
    </div>


  </div>
</template>

<script>

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

const ui = (el, filter, styles) => {
  if (typeof filter === 'function' && filter()) {
    el.removeAttribute('style');
    for (let k in styles) el.style.setProperty(k, styles[k]);
  }
}

export default {
  name: "PrettyFileManager",
  data() {
    return {
      PngDir, PngAll, PngTxt, PngCompress, PngHtml, PngJs, PngXml, PngJson, PngMd, PngCss, PngMedia,
      rootPath: '/cache/pacman/casd/casdc/dcasdcas/casd/casd/cas/dcas',
    }
  },
  created() {
    window.addEventListener("load"  , this.inflate)
    window.addEventListener("resize", this.inflate)
  },
  computed: {
    separatedRootPath() {
      return this.rootPath.split('/').filter(i => i.length !== 0)
    },
  },
  methods: {
    inflate() {
      const topLayer = this.$refs.topLayer
      const topLayerWidth = topLayer.offsetWidth
      console.info(`inflate width ${topLayerWidth} px`)
      ui(topLayer, () => topLayerWidth <= 480, {
      })
      ui(topLayer, () => topLayerWidth > 480, {
      })
    },
  }
}
</script>

<style scoped>

.central {
  display: flex;
  justify-content: center;
  align-items: center;
}

.icon-outer {
  width: 28px;
  height: 28px;
  border-radius: 28px;
  cursor: pointer;
}

.directory-level {
  transition: opacity 0.3s;
  /*margin-left: 10px;*/
  cursor: pointer;
}

</style>