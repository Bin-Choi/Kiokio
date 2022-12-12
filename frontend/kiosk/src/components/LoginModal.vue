<template>
  <Transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">
          <div class="modal-header">
            <slot name="header">로그인</slot>
          </div>

          <div class="modal-body">
            <slot name="body">
              <p v-if="error">{{ error }}</p>
              <label for="username">아이디</label>
              <input type="text" id="username" v-model="username" /><br />

              <label for="password" class="mt-2">패스워드</label>
              <input
                type="password"
                id="password"
                v-model="password"
                @keyup.enter="logIn" /><br />

              <button class="btn blue-btn mt-3" @click.stop="login">
                로그인
              </button>
              <button
                class="btn gray-btn mt-3"
                @click.stop="
                  username = null
                  password = null
                  error = null
                  $emit('close')
                ">
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
          this.error = null

          const access = res.data.access
          const refresh = res.data.refresh
          const user = res.data.user
          this.$emit('close')
          this.$store.commit('SAVE_USER', user)
          this.$store.commit('SAVE_ACCESS_TOKEN', access)
          this.$store.commit('SAVE_REFRESH_TOKEN', refresh)
        })
        .catch((err) => {
          console.error(err)
          this.password = null
        })
    },
  },
}
</script>

<style scoped>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}
.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}
.modal-container {
  width: 300px;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
}
.modal-header {
  margin-top: 0;
  color: #274894;
}
.modal-body {
  margin: 20px 0 5px 0;
}
.modal-default-button {
  float: right;
}
/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */
.modal-enter-from {
  opacity: 0;
}
.modal-leave-to {
  opacity: 0;
}
.modal-enter-from .modal-container,
.modal-leave-to .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}

input {
  background-color: rgb(203, 203, 203);
  border-radius: 0.2em;
}
</style>
