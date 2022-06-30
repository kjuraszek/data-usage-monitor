import Vue from 'vue'
import App from './App.vue'
import { router } from './router'
import { store } from './store'
import vuetify from './plugins/vuetify'
import axios from 'axios'
import axiosRetry from 'axios-retry';

axiosRetry(axios, { retries: 3,
  retryDelay: axiosRetry.exponentialDelay,
  })
Vue.prototype.$http = axios
Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
