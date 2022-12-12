<template>
  <Transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <!-- email 기입 modal -->
        <div class="modal-container">
          <div class="modal-header">
            <slot name="header">현재 이메일 : {{ user.email }}</slot>
          </div>
          <div class="modal-body">
            <slot name="body">
              <p v-if="error">{{ error }}</p>
              <label for="email">이메일</label>
              <input
                type="text"
                class="modal-input"
                id="email"
                v-model.trim="email"
              /><br />
              <button
                class="blue-btn shadow-sm"
                style="margin-right: 1vh"
                @click.stop="changeEmail"
              >
                이메일 저장
              </button>
              <button
                class="red-btn shadow-sm"
                @click.stop="
                  error = null
                  email = null
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
import axiosAuth from '@/axios/axios'

export default {
  name: 'ChangeEmailModal',
  data() {
    return {
      error: null,
      email: null,
    }
  },
  computed: {
    axios_URL() {
      return this.$store.state.axios_URL
    },
    user() {
      return this.$store.state.user
    },
  },
  methods: {
    changeEmail() {
      axiosAuth({
        method: 'put',
        url: `${this.axios_URL}/accounts/change/email/`,
        data: {
          email: this.email,
        },
        headers: {
          Authorization: `Bearer ${this.$store.state.access}`,
        },
      })
        .then((res) => {
          console.log(res)
          this.$emit('close')
          this.$store.commit('SAVE_USER_EMAIL', this.email)

          this.email = null
          this.error = null
        })
        .catch((err) => {
          console.error(err)
          this.error = err.response.data
          alert('이메일 형식을 확인해주세요')
          this.email = null
        })
    },
  },
}
</script>

<style>
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
  color: #244288;
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

.modal-input {
  background-color: #81a0bb4b;
  margin-left: 1vh;
  padding: 0.5vh;
  border-radius: 1vh;
  margin-bottom: 1.5vh;
}
</style>
