<template>
  <Transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">
          <div class="modal-header">
            <slot name="header">
              <p class="m-auto" style="font-size: 2.3vh">로그인</p>
            </slot>
          </div>

          <div class="modal-body">
            <slot name="body">
              <p v-if="error" style="color: rgb(193, 32, 42)">
                {{ error }}
              </p>
              <label for="username">아이디</label>
              <input
                type="text"
                id="username"
                class="modal-input"
                v-model="username"
              /><br />

              <label for="password">비밀번호</label>
              <input
                class="modal-input"
                type="password"
                id="password"
                v-model="password"
                @keyup.enter="logIn"
              /><br />

              <button
                class="blue-btn"
                style="margin-right: 1vh"
                @click.stop="login"
              >
                확인
              </button>
              <button
                class="red-btn"
                @click.stop="
                  username = null
                  password = null
                  error = null
                  $emit('close')
                "
              >
                취소
              </button>
            </slot>
          </div>

          <div class="modal-footer">
            <slot name="footer"> </slot>
          </div>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LoginModal',
  data() {
    return {
      username: null,
      password: null,
      error: null,
    }
  },
  computed: {
    axios_URL() {
      return this.$store.state.axios_URL
    },
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
          const refresh = res.data.refresh
          const user = res.data.user
          this.$emit('close')
          this.$store.commit('SAVE_USER', user)
          this.$store.commit('SAVE_ACCESS_TOKEN', access)
          this.$store.commit('SAVE_REFRESH_TOKEN', refresh)
        })
        .catch((err) => {
          const status = err.response.status

          if (status === 404) {
            this.error = '해당 아이디 정보가 없습니다.'
          } else if (status === 400) {
            this.error = '비밀번호가 틀렸습니다.'
          }
          this.password = null
        })
    },
  },
}
</script>

<style scoped>
input {
  width: 40%;
}
</style>
