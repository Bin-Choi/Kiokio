<template>
  <Transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <!-- email 기입 modal -->
        <div v-if="!user.email" class="modal-container">
          <div class="modal-header">
            <slot name="header"
              >이메일을 먼저 설정해주세요. (비밀번호를 잃어버렸을 경우, 해당
              이메일로 재설정할 수 있습니다.)</slot
            >
          </div>
          <div class="modal-body">
            <slot name="body">
              <p v-if="error">{{ error }}</p>
              <label for="email">이메일</label>
              <input type="text" id="email" v-model.trim="email" /><br />
              <button class="btn blue-btn mt-3" @click.stop="saveEmail">
                이메일 저장
              </button>
              <button
                class="btn gray-btn mt-3"
                @click.stop="
                  error = null
                  email = null
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

        <!-- 비밀번호 변경 modal -->
        <div v-if="user.email" class="modal-container">
          <div class="modal-header">
            <slot name="header">비밀번호 변경</slot>
          </div>
          <div class="modal-body">
            <slot name="body">
              <p v-if="error">{{ error }}</p>
              <label for="oldPassword">기존 비밀번호</label>
              <input
                type="password"
                id="oldPassword"
                v-model.trim="oldPassword" /><br />
              <label for="password1">새 비밀번호</label>
              <input
                type="password"
                id="newPassword1"
                v-model.trim="newPassword1" /><br />
              <label for="password2">새 비밀번호 확인</label>
              <input
                type="password"
                id="new_password2"
                v-model.trim="newPassword2" /><br />
              <button class="btn blue-btn mt-3" @click.stop="changePassword">
                비밀번호 변경
              </button>
              <button
                class="btn gray-btn mt-3"
                @click.stop="
                  error = null
                  oldPassword = null
                  newPassword1 = null
                  newPassword2 = null
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
import axiosAuth from '@/axios/axios'

export default {
  name: 'ChangePasswordModal',
  data() {
    return {
      error: null,
      email: null,
      oldPassword: null,
      newPassword1: null,
      newPassword2: null,
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
    saveEmail() {
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
    changePassword() {
      if (this.password1 !== this.password2) {
        alert('비밀번호가 일치하지 않습니다')
        return
      }
      axiosAuth({
        method: 'post',
        url: `${this.axios_URL}/dj-rest-auth/password/change/`,
        data: {
          old_password: this.oldPassword,
          new_password1: this.newPassword1,
          new_password2: this.newPassword2,
        },
        headers: {
          Authorization: `Bearer ${this.$store.state.access}`,
        },
      })
        .then((res) => {
          console.log(res)
          this.$emit('close')
          alert('비밀번호가 변경되었습니다.')
        })
        .catch((err) => {
          console.error(err)
          this.error = err.response.data
          alert('비밀번호를 다시 확인해주세요')
          this.password1 = null
          this.password2 = null
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
