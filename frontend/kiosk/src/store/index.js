import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    axios_URL: 'http://127.0.0.1:8000',
    studentPk: null,
  },
  getters: {},
  mutations: {
    STUDENT_INFO(state, payload) {
      state.studentPk = payload;
    },
  },
  actions: {},
  modules: {},
});
