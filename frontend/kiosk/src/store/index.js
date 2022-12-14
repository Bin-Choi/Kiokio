import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'
import jwt_decode from 'jwt-decode'
import axiosAuth from '@/axios/axios'

// import SecureLS from 'secure-ls'
// const ls = new SecureLS({ isCompression: false })

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState({
      // storage: {
      //   getItem: (key) => ls.get(key),
      //   setItem: (key, value) => ls.set(key, value),
      //   removeItem: (key) => ls.remove(key),
      // },
      // BlckList
      reducer: (persistedState) => {
        const stateFilter = Object.assign({}, persistedState)
        const blackList = ['axios_URL', 'showLoginModal', 'inbodyStudents']
        blackList.forEach((item) => {
          delete stateFilter[item]
        })
        return stateFilter
      },
    }),
  ],
  state: {
    axios_URL: 'http://127.0.0.1:8000',
    user: null,
    access: null,
    refresh: null,

    showLoginModal: false,
    showChangePasswordModal: false,
    showChangeEmailModal: false,
    inbodyStudents: null,
    student: null,
    inbody: null,
  },
  getters: {
    // 메서드를 통한 getters 요청은 캐시되지 않으며, 요청시마다 재실행. now = Date.now()
    isLogin: (state) => (now) => {
      // refresh 토큰이 없으면
      if (!state.refresh) {
        return false
      }
      // refresh 토큰의 유효기간 30분 남았으면
      const decoded = jwt_decode(state.refresh)
      const exp = decoded.exp
      if (now - 30 * 60 * 1000 >= exp * 1000) {
        return false
      }
      // 그 외는 로그인했음
      return true
    },
  },
  mutations: {
    STUDENT_INFO(state, student) {
      state.student = student
    },
    INBODY_INFO(state, inbody) {
      state.inbody = inbody
    },
    SAVE_ACCESS_TOKEN(state, access) {
      state.access = access
    },
    SAVE_REFRESH_TOKEN(state, refresh) {
      state.refresh = refresh
    },
    SAVE_USER(state, user) {
      state.user = user
    },
    SAVE_USER_EMAIL(state, email) {
      state.user.email = email
    },
    DELETE_TOKENS(state) {
      state.access = null
      state.refresh = null
    },
    SAVE_ID_PASSWORD(state, payload) {
      const { id, password } = payload
      state.student.id = id
      state.student.password = password
    },
    SAVE_INBODY_STUDENTS(state, students) {
      state.inbodyStudents = students
    },
    CHANGE_STUDENT_INBODY(state, payload) {
      const { studentIndex, inbodyList } = payload
      state.inbodyStudents[studentIndex].inbody_set = inbodyList
    },
    CHANGE_STUDENT_INBODY_DETAIL(state, payload) {
      const { studentIndex, inbodyIndex, inbody } = payload
      state.inbodyStudents[studentIndex].inbody_set[inbodyIndex] = inbody
    },
    DELETE_STUDENT_INBODY_DETAIL(state, payload) {
      const { studentIndex, inbodyIndex } = payload
      state.inbodyStudents[studentIndex].inbody_set.splice(inbodyIndex, 1)
    },
    TOGGLE_SHOW_LOGIN_MODAL(state, boolean) {
      state.showLoginModal = boolean
    },
    TOGGLE_SHOW_CHANGE_PASSWORD_MODAL(state, boolean) {
      state.showChangePasswordModal = boolean
    },
    TOGGLE_SHOW_CHANGE_EMAIL_MODAL(state, boolean) {
      state.showChangeEmailModal = boolean
    },
  },
  actions: {
    logout(context) {
      axiosAuth({
        method: 'post',
        url: `${context.state.axios_URL}/accounts/logout/`,
        headers: {
          Authorization: `Bearer ${context.state.access}`,
        },
      })
        .then(() => {
          // console.log(res)
          context.commit('DELETE_TOKENS')
          router.push({ name: 'login' })
        })
        .catch(() => {
          // refresh 토큰이 만료되었을 경우, 그냥 클라이언트 토큰만 삭제해버림
          // console.error(err)
          context.commit('DELETE_TOKENS')
          router.push({ name: 'login' })
        })
    },
    refresh(context) {
      axios({
        method: 'post',
        url: `${context.state.axios_URL}/accounts/refresh/`,
        data: {
          user_id: context.state.userId,
          refresh: context.state.refresh,
        },
      })
        .then((res) => {
          // console.log(res)
          const access = res.data.access
          context.commit('SAVE_ACCESS_TOKEN', access)
        })
        .catch((err) => {
          console.error(err)
        })
    },
  },
})
