import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import Register from '@/views/RegisterView.vue'
import Login from '@/views/LoginView.vue'
import Dashboard from '@/views/DashboardView.vue'
import Profile from '@/views/ProfileView.vue'
import NoteView from '@/views/NoteView.vue'
import EditNoteView from '@/views/EditNoteView.vue'
// import store from '@/store'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: { requiresAuth: true },
  },
  {
    path: '/note/:id',
    name: 'Note',
    component: NoteView,
    meta: { requiresAuth: true },
    props: true
  },
  {
    path: '/editnote/:id',
    name: 'EditNote',
    component: EditNoteView,
    meta: { requiresAuth: true },
    props: true
  },
  {
    path: '/profile',
    name: 'Profile',
    meta: { requiresAuth: true },
    component: Profile
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// TODO: later
// router.beforeEach((to, _, next) => {
//   if (to.matched.some(record => record.meta.requiresAuth)) {
//     console.log(store);
//     if (store.getters.isAuthenticated) {
//       next();
//       return;
//     }
//     next('/login');
//   } else {
//     next();
//   }
// });


export default router
