<template>
  <div style="position: absolute; top: 0; bottom: 0; left: 0; right: 0; background: #f5f7fd; margin: 0; padding: 0; font-family: Roboto, Helvetica, sans-serif; overflow: hidden;">
    <div class="header">
      <div style="width: 100%; height: calc(100% - 1px); border-bottom: 1px solid #ddd;">

      </div>
    </div>

    <div class="navigator">
      <div style="width: calc(100% - 1px); height: 100%; border-right: 1px solid #ddd; overflow: auto;">
        <div style="width: 100%; height: calc(100% - 32px);">

        </div>
        <div style="width: calc(100% - 20px); margin: 0 10px; height: calc(32px - 1px); line-height: 31px; border-top: 1px solid #ddd; text-align: center; font-size: 12px; color: #888;">
          <div style="display: inline-block; width: 14px; height: 14px; position: relative; top: 2px;">
            <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" style="width: 100%;" fill="#888">
              <path d="M726.4 201.6c-12.8-9.6-28.8-6.4-38.4 0-9.6 9.6-16 25.6-9.6 38.4 6.4 12.8 9.6 28.8 12.8 44.8-86.4-201.6-230.4-246.4-236.8-249.6-9.6-3.2-22.4 0-28.8 6.4-9.6 6.4-12.8 19.2-9.6 28.8 12.8 86.4-25.6 188.8-115.2 310.4-6.4-25.6-16-51.2-32-80-9.6-9.6-22.4-16-35.2-12.8-16 3.2-25.6 12.8-25.6 28.8-3.2 48-25.6 92.8-51.2 140.8-22.4 41.6-44.8 86.4-54.4 134.4-32 153.6 35.2 265.6 224 368 6.4 3.2 9.6 3.2 16 3.2 9.6 0 19.2-6.4 25.6-12.8 9.6-16 6.4-35.2-9.6-44.8l-3.2-3.2c-188.8-105.6-214.4-192-192-297.6 9.6-41.6 28.8-76.8 48-118.4 12.8-19.2 22.4-38.4 28.8-57.6 0 9.6 3.2 22.4 3.2 32 0 12.8 9.6 25.6 22.4 28.8 12.8 3.2 25.6 0 35.2-9.6 112-134.4 172.8-256 179.2-364.8 51.2 32 137.6 108.8 182.4 272 3.2 9.6 9.6 19.2 22.4 22.4 9.6 3.2 22.4 0 28.8-6.4 25.6-22.4 38.4-54.4 41.6-86.4 54.4 67.2 115.2 176 108.8 288-6.4 92.8-57.6 172.8-150.4 243.2 35.2-166.4-32-358.4-179.2-457.6-9.6-6.4-22.4-6.4-32-3.2-9.6 6.4-16 16-16 28.8-3.2 89.6-48 144-89.6 198.4-35.2 44.8-70.4 89.6-76.8 150.4 0 16 12.8 32 28.8 35.2 19.2 3.2 32-12.8 35.2-28.8 3.2-41.6 32-76.8 60.8-115.2 35.2-44.8 76.8-99.2 96-176 115.2 108.8 153.6 300.8 83.2 435.2v3.2c0 3.2 0 3.2-3.2 6.4v12.8c0 3.2 0 3.2 3.2 6.4v3.2l3.2 3.2c0 3.2 3.2 3.2 3.2 6.4 0 0 3.2 3.2 6.4 3.2l3.2 3.2s3.2 0 3.2 3.2h19.2c3.2 0 6.4 0 9.6-3.2 163.2-89.6 252.8-208 259.2-345.6 9.6-214.4-169.6-393.6-204.8-416z"></path>
            </svg>
          </div>
          Author Jun.Dai
        </div>
      </div>

    </div>

    <div class="article" :style="{right: `${descPageState ? 300 : 0}px`}">

      <div style="margin: 50px;">
        <div class="pretty-button" @click="changeDescPageState">description</div>
      </div>

      <div style="position: absolute; height: 32px; bottom: 0; left: 0; right: 0;">
        <div style="width: calc(100% - 20px); margin: 0 10px; height: calc(32px - 1px); line-height: 31px; border-top: 1px solid #ddd; text-align: center; font-size: 12px; color: #888;">
          Copyright © 2022. All rights reserved.
        </div>
      </div>

    </div>

    <div class="description" :style="{right: `${descPageState ? '0' : '-300px'}`}">
      <div style="width: calc(100% - 1px); height: 100%; border-left: 1px solid #ddd;">

      </div>
    </div>
  </div>
</template>

<script>

import "@/fonts/roboto/roboto.css"

export default {
  name: "Dashboard",
  data() {
    return {
      descPageState: false,
    }
  },
  computed: {

  },
  methods: {
    changeDescPageState() {
      this.descPageState = !this.descPageState
    }
  }
}
</script>

<style scoped>

.header {
  width: 100%;
  height: 70px;
  z-index: 3;
}

.navigator {
  position: absolute;
  top: 70px;
  width: 300px;
  height: calc(100% - 70px);
  z-index: 2;
}

.article {
  transition: right 0.3s;
  position: absolute;
  top: 70px;
  left: 300px;
  bottom: 0;
  z-index: 1;
}

.description {
  transition: right 0.3s;
  position: absolute;
  top: 70px;
  bottom: 0;
  width: 300px;
}

.pretty-button {
  display: inline-block;
  height: 32px;
  line-height: 32px;
  padding-left: 16px;
  padding-right: 16px;
  border-radius: 6px;
  background-color: #409eff;
  color: #fff;
  cursor: pointer;
}

.pretty-button:hover {
  background-color: #0079fe;
}

</style>