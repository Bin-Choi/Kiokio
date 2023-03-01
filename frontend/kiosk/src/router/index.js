import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store/index.js'
// Admin Page
import AdminView from '@/views/admin/AdminView'
import LoginView from '@/views/admin/LoginView'
import StudentView from '@/views/admin/StudentView'
import AttendanceView from '@/views/admin/AttendanceView'
// import StudentCreateView from '@/views/admin/StudentCreateView'
import AdminInbodyView from '@/views/admin/AdminInbodyView'
import InbodyDateView from '@/views/admin/InbodyDateView'

import StudentRead from '@/components/admin/student/StudentRead'

// Kiosk Page
import IndexView from '@/views/kiosk/IndexView'
import AttendCheckView from '@/views/kiosk/AttendCheckView'
import InbodyView from '@/views/kiosk/InbodyView'
import InbodyDetailView from '@/views/kiosk/InbodyDetailView'
import InbodyCreateView from '@/views/kiosk/InbodyCreateView'
import InbodyHistoryView from '@/views/kiosk/InbodyHistoryView'
import InbodyUpdateView from '@/views/kiosk/InbodyUpdateView'
import PasswordUpdateView from '@/views/kiosk/PasswordUpdateView'
import GymView from '@/views/kiosk/GymView'

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
    children: [
      {
        path: '',
        component: StudentRead,
      },
    ],
    beforeEnter(to, from, next) {
      if (store.getters.isLogin(Date.now())) {
        next()
      } else {
        alert('로그인 해주세요')
        router.push({ name: 'login' })
      }
    },
  },
  // {
  //   path: '/student/create',
  //   name: 'studentCreate',
  //   component: StudentCreateView,
  //   beforeEnter(to, from, next) {
  //     if (store.getters.isLogin(Date.now())) {
  //       next()
  //     } else {
  //       alert('로그인 해주세요')
  //       router.push({ name: 'login' })
  //     }
  //   },
  // },
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
    path: '/admin/inbody/date',
    name: 'adminInbodyDate',
    component: InbodyDateView,
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
    component: AttendCheckView,
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
