// ./frontend/src/main.js

// Укажем путь до bootstrap
import 'bootstrap/dist/css/bootstrap.css';
import axios from 'axios'
import Vue from 'vue'

import App from './App.vue'
import router from './router'

axios.defaults.withCredentials = true;
// Укажем хост до backend-а
axios.defaults.baseURL = 'http://localhost:5000/';
Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
