import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store/index.js'

import IndexView from '@/views/IndexView'
import AdminView from '@/views/AdminView'
import LoginView from '@/views/LoginView'
import StudentView from '@/views/StudentView'
import AttendanceView from '@/views/AttendanceView'
import StudentCreateView from '@/views/StudentCreateView'
import AdminInbodyView from '@/views/AdminInbodyView'

import AttendView from '@/views/AttendView'

import GymView from '@/views/GymView'

import InbodyView from '@/views/InbodyView'
import InbodyDetailView from '@/views/InbodyDetailView'
import InbodyCreateView from '@/views/InbodyCreateView'
import InbodyHistoryView from '@/views/InbodyHistoryView'
import InbodyUpdateView from '@/views/InbodyUpdateView'

import PasswordUpdateView from '@/views/PasswordUpdateView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'index',
    component: IndexView,
    beforeEnter(to, from, next) {
      store.state.user = null
      store.state.access = null
      store.state.refresh = null
      store.state.student = null
      store.state.inbody = null
      next()
    },
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    beforeEnter(to, from, next) {
      store.state.user = null
      store.state.access = null
      store.state.refresh = null
      next()
    },
  },
  {
    path: '/admin',
    name: 'admin',
    component: AdminView,
  },
  {
    path: '/student',
    name: 'student',
    component: StudentView,
    beforeEnter(to, from, next) {
      if (store.getters.isLogin(Date.now())) {
        next()
      } else {
        alert('로그인 해주세요')
        router.push({ name: 'login' })
      }
    },
  },
  {
    path: '/student/create',
    name: 'studentCreate',
    component: StudentCreateView,
    beforeEnter(to, from, next) {
      if (store.getters.isLogin(Date.now())) {
        next()
      } else {
        alert('로그인 해주세요')
        router.push({ name: 'login' })
      }
    },
  },
  {
    path: '/attendance',
    name: 'attendance',
    component: AttendanceView,
    beforeEnter(to, from, next) {
      if (store.getters.isLogin(Date.now())) {
        next()
      } else {
        alert('로그인 해주세요')
        router.push({ name: 'login' })
      }
    },
  },
  {
    path: '/admin/inbody',
    name: 'adminInbody',
    component: AdminInbodyView,
    beforeEnter(to, from, next) {
      if (store.getters.isLogin(Date.now())) {
        next()
      } else {
        alert('로그인 해주세요')
        router.push({ name: 'login' })
      }
    },
  },
  {
    path: '/attend',
    name: 'attend',
    component: AttendView,
  },
  {
    path: '/inbody',
    name: 'inbody',
    component: InbodyView,
    beforeEnter(to, from, next) {
      store.state.student = null
      store.state.inbody = null
      next()
    },
  },
  {
    path: '/gym',
    name: 'gym',
    component: GymView,
  },
  {
    path: '/inbody/detail',
    name: 'inbodyDetail',
    component: InbodyDetailView,
  },
  {
    path: '/inbody/update',
    name: 'inbodyUpdate',
    component: InbodyUpdateView,
  },
  {
    path: '/inbody/create',
    name: 'inbodyCreate',
    component: InbodyCreateView,
  },
  {
    path: '/inbody/history',
    name: 'inbodyHistory',
    component: InbodyHistoryView,
  },
  {
    path: '/password/update',
    name: 'passwordUpdate',
    component: PasswordUpdateView,
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
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})

export default router
