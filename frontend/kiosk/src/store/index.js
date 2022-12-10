import Vue from "vue"
import Vuex from "vuex"
import axios from "axios"
import createPersistedState from "vuex-persistedstate"

import SecureLS from "secure-ls"
import router from "@/router"
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
      whiteList: ["access"],
    }),
  ],
  state: {
    axios_URL: "http://127.0.0.1:8000",
    access: null,
    inbodyStudents: null,

    passwordToken: null,

    student: null,
    inbody: null,
  },
  getters: {},
  mutations: {
    STUDENT_INFO(state, payload) {
      state.student = payload
    },
    INBODY_INFO(state, payload) {
      state.inbody = payload
    },
    SAVE_TOKEN(state, access) {
      state.access = access
    },
    DELETE_TOKEN(state) {
      state.access = null
    },
    SAVE_PW_TOKEN(state, token) {
      state.passwordToken = token
      console.log(state.passwordToken)
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
  },
  actions: {
    logout(context) {
      axios({
        method: "post",
        url: `${context.state.axios_URL}/accounts/logout/`,
        headers: {
          Authorization: `Bearer ${context.state.access}`,
        },
      })
        .then((res) => {
          console.log(res)
          context.commit("DELETE_TOKEN")
          router.push({ name: "login" })
        })
        .catch((err) => {
          console.error(err)
        })
    },
  },
})
