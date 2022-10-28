<template>
  <div ref="topLayer" style="width: 100%; margin: 0; padding: 0; position: relative;">
    <div ref="header" style="position: fixed; top: 0; left: 0; right: 0; width: 100%; height: 60px; background-color: white; box-shadow: 0 1px 3px rgba(23,24,25,0.2)">

      <div ref="avatar" :style="{right: isPhoneSize ? 'auto': '20px', left: isPhoneSize ? '20px' : 'auto'}"
           class="central"
           style="height: 100%; position: absolute; top: 0;">
        <div class="central" style="width: 32px; height: 32px; border-radius: 32px; background-color: #f8aba6; cursor: pointer;">
          <img style="width: 90%; height: 90%;" :src="SvgSpaceDog" alt="" />
        </div>

<!--        <div style="position: relative;">-->
<!--          <ul>-->
<!--            <li>logout</li>-->
<!--          </ul>-->
<!--        </div>-->
      </div>

      <div ref="logo" class="central" style="position: absolute; top: 0; left: 0; height: 100%; user-select: none; cursor: pointer;">
        <div>
          <span class="logo-text-0">Stars</span>
          <span class="logo-text-1">Picking</span>
        </div>
      </div>

      <div ref="navMenu" v-if="isPhoneSize" style="display: flex; justify-content: center; align-items: center; height: 100%; position: absolute; top: 0; right: 20px;">
        <img :src="SvgMenu" alt="" style="width: 24px; height: 24px; cursor: pointer;" @click="clickMenu"/>
      </div>
    </div>

    <div ref="navigator" style="padding: 10px; background-color: #E0C3FC; z-index: -1;">
      <ul style="margin: 0; padding: 0; width: 100%;">
        <li class="nav-item">
          <img class="nav-icon" :src="SvgHome" alt="" />
          <span class="nav-text">Home</span>
        </li>
        <li class="nav-item">
          <img class="nav-icon" :src="SvgHome" alt="" />
          <span class="nav-text">Monitor</span>
        </li>
        <li class="nav-item">
          <img class="nav-icon" :src="SvgHome" alt="" />
          <span class="nav-text">User</span>
        </li>
      </ul>

    </div>

    <div ref="composedArea">
      <h1>buhcasdbcsaS</h1>
    </div>
  </div>
</template>

<script>
import SvgSpaceDog from "@/assets/space_dog.svg"
import SvgMenu from "@/ikonate/list.svg"
import SvgHome from "@/ikonate/home.svg"

const PHONE_WIDTH = 480

export default {
  name: "AppStarsPicking",
  created() {
    window.addEventListener("load"  , this.ui)
    window.addEventListener('resize', this.ui)
  },
  data() {
    return {
      SvgSpaceDog,
      SvgMenu, SvgHome,
      topLayerWidth: 0,
      menuState: false,
      iPage: 0,
    }
  },
  computed: {
    isPhoneSize() {
      return this.topLayerWidth <= PHONE_WIDTH
    }
  },
  methods: {
    ui() {
      const topLayer      = this.$refs.topLayer
      const header        = this.$refs.header
      const navigator     = this.$refs.navigator
      const composedArea  = this.$refs.composedArea
      const navMenu       = this.$refs.navMenu
      this.topLayerWidth  = topLayer.offsetWidth
      // console.info('ui')
      if (this.isPhoneSize) {
        // phone size
        this.$refs.logo.style.width = '100%'
        navigator.style.position = 'fixed'
        navigator.style.overflow = 'hidden'
        navigator.style.height = 'auto'
        navigator.style.transition = 'top 0.5s'
        navigator.style.top = this.menuState ? '60px' : `${60 - navigator.offsetHeight}px`
        navigator.style.left = '0'
        navigator.style.bottom = 'auto'
        navigator.style.width = 'calc(100% - 20px)'
      } else {
        // computer size
        this.$refs.logo.style.width = '240px'
        navigator.style.position = 'fixed'
        navigator.style.overflow = 'auto'
        navigator.style.height = 'auto'
        navigator.style.transition = 'none'
        navigator.style.top = '60px'
        navigator.style.left = '0'
        navigator.style.bottom = '0'
        navigator.style.width = 'calc(240px - 20px)'

        composedArea.style.position = 'relative'
        composedArea.style.marginLeft = '260px'
        composedArea.style.paddingTop = '60px'
      }
    },
    clickMenu() {
      this.menuState = !this.menuState
      if (this.isPhoneSize) {
        this.$refs.navigator.style.top = this.menuState ? '60px' : `${60 - this.$refs.navigator.offsetHeight}px`
      }
    }
  }
}
</script>

<style scoped>


.logo-text-0 { font-size: 20px; font-weight: bold; color: white; background: linear-gradient(110deg, #8EC5FC, #E0C3FC); border-radius: 8px; padding: 3px 10px; }
.logo-text-1 { font-size: 20px; font-weight: bold; margin-left: 5px; background: linear-gradient(110deg, #8EC5FC, #E0C3FC); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }

.central {
  display: flex; justify-content: center; align-items: center;
}

li {
  text-decoration: none;
}

.nav-text {
  width: calc(100% - 20px);
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow-x: hidden;
}

.nav-item {
  width: calc(100% - 20px);
  display: flex;
  align-items: center;
  padding: 10px 10px;
  cursor: pointer;
  border-radius: 10px;
}

.nav-item:hover {
  background-color: rgba(0,0,0,0.1);
}

.nav-icon {
  width: 20px;
  height: 20px;
  margin-right: 10px;
}

</style>