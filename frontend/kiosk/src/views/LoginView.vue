<template>
  <div
    class="d-flex flex-column align-items-center"
    style="width: 100vw; height: 100vh; padding: 7vh">
    <div class="d-flex justify-content-start w-100">
      <div @click="$router.push({ name: 'index' })" style="cursor: pointer">
        <font-awesome-icon icon="fa-solid fa-house" />
        <span>키오스크 홈</span>
      </div>
    </div>

    <div style="margin-top: 10vh; font-size: 4vh">
      00초등학교 키오스크 관리자 페이지
    </div>

    <!-- 로그인 -->
    <div
      class="d-flex flex-column justify-content-between bg-light rounded shadow"
      style="
        width: 50vw;
        height: 30vh;
        margin-top: 10vh;
        padding-top: 5vh;
        padding-bottom: 5vh;
        font-size: 2.5vh;
      ">
      <div>
        <span>아이디 </span>
        <input
          type="text"
          class="shadow rounded"
          ref="username"
          v-model="username"
          @keyup.enter="$refs.password.focus()" />
      </div>
      <div>
        <span>비밀번호 </span>
        <input
          type="password"
          class="shadow rounded"
          ref="password"
          v-model="password"
          @keyup.enter="login" />
      </div>
      <div>
        <button type="button" class="btn btn-primary shadow" @click="login">
          로그인
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LoginView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  computed: {
    axios_URL() {
      return this.$store.state.axios_URL
    },
  },
  mounted() {
    this.$refs.username.focus()
  },
  methods: {
    login() {
      axios({
        method: 'post',
        url: `${this.axios_URL}/accounts/login/`,
        data: {
          username: this.username,
          password: this.password,
        },
      })
        .then((res) => {
          console.log(res)
          this.username = null
          this.password = null

          const access = res.data.access
          this.$store.commit('SAVE_TOKEN', access)
          this.$router.push({ name: 'admin' })
        })
        .catch((err) => {
          console.error(err)
          this.password = null
        })
    },
  },
}
</script>

<style></style>
