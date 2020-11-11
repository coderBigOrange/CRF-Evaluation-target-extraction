import Vue from 'vue'
import App from './App.vue'
import ElementUi from 'element-ui'
import store from "./store/store";
import './plugins/element.js'
import 'element-ui/lib/theme-chalk/index.css'
import router from './router'

Vue.use(ElementUi)
Vue.config.productionTip = false

new Vue({
  el:'#app',
  router,
  store,
  render: h => h(App)
});
