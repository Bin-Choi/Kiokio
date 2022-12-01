import Vue from "vue"
import VueRouter from "vue-router"

import IndexView from "@/views/IndexView"
import AdminView from "@/views/AdminView"
import AttendView from "@/views/AttendView"
import InbodyView from "@/views/InbodyView"
import GymView from "@/views/GymView"
import InbodyDetailView from "@/views/InbodyDetailView"
import InbodyFormView from "@/views/InbodyFormView"

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    name: "index",
    component: IndexView,
  },
  {
    path: "/admin",
    name: "admin",
    component: AdminView,
  },
  {
    path: "/attend",
    name: "attend",
    component: AttendView,
  },
  {
    path: "/inbody",
    name: "inbody",
    component: InbodyView,
  },
  {
    path: "/gym",
    name: "gym",
    component: GymView,
  },
  {
    path: "/inbody/detail",
    name: "inbodyDetail",
    component: InbodyDetailView,
  },
  {
    path: "/inbody/form",
    name: "inbodyForm",
    component: InbodyFormView,
  },

  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  // }
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
})

export default router
