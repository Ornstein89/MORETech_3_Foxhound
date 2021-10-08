import Vue from 'vue'
import VueRouter from 'vue-router'


Vue.use(VueRouter)

let opts = {
  routes: [
    {
      path: "/",
      name: "Home",
      component: () => import('../views/Home.vue'),
      meta: {
        requiresAuth: false
      }
    },
    {
      path: "/login",
      name: "login",
      component: () => import('../views/Login.vue'),
      meta: {
        requiresAuth: false
      }
    },
    {
      path: "/profile",
      name: "Profile",
      component: () => import('../views/Profile.vue'),
      meta: {
        requiresAuth: false
      },
    },
    {
      path: "/graph",
      name: "Graph",
      component: () => import('../views/Editor.vue'),
      meta: {
        requiresAuth: false
      },
    },
  ],
  linkExactActiveClass: 'active'
};
const router = new VueRouter(opts);

export default router