import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)


export default new Vuex.Store({
  state: {
    student:null,
  },
  getters: {
  },
  mutations: {
    STUDENT_INFO(state,payload){
      state.student = payload
    }
  },
  actions: {

  },
  modules: {
  }
})
