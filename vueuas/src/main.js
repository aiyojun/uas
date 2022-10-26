import Vue from 'vue'
import App from './App.vue'
import Login from './components/Login.vue'
import FileManager from './components/FileManager.vue'

Vue.config.productionTip = false

new Vue({
  render: h => h(FileManager),
}).$mount('#app')
