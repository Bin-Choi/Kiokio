<template>
  <div
    class="bg-white d-flex flex-column align-items-center"
    style="padding: 7vh; height: 100vh; width: 100vw"
  >
    <div class="w-100 d-flex justify-content-between">
      <div @click="toResetPassword" style="cursor: pointer">
        <font-awesome-icon
          class="icon"
          icon="fa-solid fa-lock"
          style="font-size: 3vh"
        />
        <div>비밀번호 초기화</div>
      </div>
      <div @click="$router.push({ name: 'index' })" style="cursor: pointer">
        <font-awesome-icon
          class="icon"
          icon="fa-solid fa-house"
          style="font-size: 3vh"
        />
        <div>키오스크 홈</div>
      </div>
    </div>

    <div
      class="d-flex flex-column align-items-center justify-content-around"
      style="width: 75vw; height: 50vh; margin-top: 10vh"
    >
      <div style="font-size: 3.7vh; padding: 1vh 2vh">
        00초등학교 키오스크 관리자 페이지
      </div>

      <!-- 로그인 -->
      <div
        id="login"
        class="d-flex flex-column rounded shadow justify-content-center"
      >
        <div class="w-75 d-flex justify-content-between">
          <div>아이디</div>
          <input
            type="text"
            class="rounded bg-white shadow-sm"
            ref="username"
            v-model="username"
            @keyup.enter="$refs.password.focus()"
          />
        </div>

        <div class="w-75 d-flex justify-content-between">
          <div>비밀번호</div>
          <input
            type="password"
            class="rounded bg-white shadow-sm"
            ref="password"
            v-model="password"
            @keyup.enter="login"
          />
        </div>

        <div>
          <button
            type="button"
            class="btn shadow text-white"
            style="margin-top: 1vh; background-color: #6396c3; font-size: 2.2vh"
            @click="login"
          >
            로그인
          </button>
        </div>
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
        withCredentials: true,
      })
        .then((res) => {
          console.log(res)
          this.username = null
          this.password = null

          const access = res.data.access
          const refresh = res.data.refresh
          const user = res.data.user
          this.$store.commit('SAVE_USER', user)
          this.$store.commit('SAVE_ACCESS_TOKEN', access)
          this.$store.commit('SAVE_REFRESH_TOKEN', refresh)
          this.$router.push({ name: 'admin' })
        })
        .catch((err) => {
          console.log(err)
          const {
            response: { status },
          } = err
          if (status === 404) {
            alert('해당 아이디 정보가 없습니다')
          } else if (status === 400) {
            alert('비밀번호를 다시 입력해주세요')
          }
          this.password = null
        })
    },
    toResetPassword() {
      window.open(`${this.axios_URL}/django/password_reset/`)
    },
  },
}
</script>

<style scoped>
input {
  width: 50%;
  padding: 0.5vh;
  font-size: 2vh;
}

#login {
  background-color: #2b64aa1e;
  text-align: center;
  font-size: 2.5vh;
  width: 40%;
  height: 60%;
  padding: 2vh 1vh;
}

#login div {
  margin: 1vh auto;
}
</style>
