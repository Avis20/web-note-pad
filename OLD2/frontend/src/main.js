// ./frontend/src/main.js

// Укажем путь до bootstrap
import 'bootstrap/dist/css/bootstrap.css';
import axios from 'axios'
import Vue from 'vue'

import App from './App.vue'
import router from './router'
import store from './store'

axios.defaults.withCredentials = true;
// Укажем хост до backend-а
axios.defaults.baseURL = process.env.VUE_APP_BACKEND_HOST;
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
