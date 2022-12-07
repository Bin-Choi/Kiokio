import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'

import SecureLS from 'secure-ls'
import router from '@/router'
const ls = new SecureLS({ isCompression: false })

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState({
      storage: {
        getItem: (key) => ls.get(key),
        setItem: (key, value) => ls.set(key, value),
        removeItem: (key) => ls.remove(key),
      },
      whiteList: ['access'],
    }),
  ],
  state: {
    axios_URL: 'http://127.0.0.1:8000',
    access: null,
    student: null,
  },
  getters: {},
  mutations: {
    STUDENT_INFO(state, payload) {
      state.student = payload
    },
    SAVE_TOKEN(state, access) {
      state.access = access
    },
    DELETE_TOKEN(state) {
      state.access = null
    },
  },
  actions: {
    logout(context) {
      axios({
        method: 'post',
        url: `${context.state.axios_URL}/accounts/logout/`,
        headers: {
          Authorization: `Bearer ${context.state.access}`,
        },
      })
        .then((res) => {
          console.log(res)
          context.commit('DELETE_TOKEN')
          router.push({ name: 'login' })
        })
        .catch((err) => {
          console.error(err)
        })
    },
  },
})
