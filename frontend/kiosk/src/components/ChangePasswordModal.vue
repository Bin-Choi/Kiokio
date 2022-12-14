<template>
  <Transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <!-- email 기입 modal -->
        <div v-if="!user.email" class="modal-container">
          <div class="modal-header">
            <slot name="header">
              이메일을 먼저 설정해주세요. <br />
              (비밀번호를 잃어버렸을 경우, 해당 이메일로 재설정할 수 있습니다.)
            </slot>
          </div>
          <div class="modal-body">
            <slot name="body">
              <p v-if="error" style="color: rgb(193, 32, 42)">
                {{ error }}
              </p>
              <label for="email">이메일</label>
              <input
                type="text"
                id="email"
                v-model.trim="email"
                class="modal-input"
              /><br />

              <button
                class="blue-btn shadow-sm"
                style="margin-right: 1vh"
                @click.stop="saveEmail"
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

        <!-- 비밀번호 변경 modal -->
        <div v-if="user.email" class="modal-container">
          <div class="modal-header">
            <slot name="header">
              <div class="m-auto" style="font-size: 3vh">비밀번호 변경</div>
            </slot>
          </div>

          <div class="modal-body">
            <slot name="body">
              <!-- ERROR -->
              <div
                v-if="error && typeof error === 'object'"
                style="color: rgb(193, 32, 42)"
              >
                <p
                  v-for="(err, idx) in error"
                  :key="idx"
                  style="margin: 0; padding: 0"
                >
                  {{ err }}
                </p>
              </div>
              <div
                v-if="error && typeof error === 'string'"
                style="color: rgb(193, 32, 42)"
              >
                {{ error }}
              </div>

              <!-- PASSWORD FORM -->
              <label for="newPassword1">새 비밀번호</label> <br />
              <input
                type="password"
                id="newPassword1"
                class="modal-input"
                v-model.trim="newPassword1"
              /><br />

              <label for="newPassword2">새 비밀번호 확인</label>
              <input
                type="password"
                id="newPassword2"
                class="modal-input"
                v-model.trim="newPassword2"
                @keyup.enter="changePassword"
              /><br />

              <button
                class="blue-btn shadow-sm"
                style="margin-right: 1vh"
                @click="changePassword"
              >
                확인
              </button>
              <button
                class="red-btn shadow-sm"
                @click="
                  error = null
                  newPassword1 = null
                  newPassword2 = null
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
  name: 'ChangePasswordModal',
  data() {
    return {
      error: null,
      email: null,
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
      if (!this.email) {
        this.error = '이메일을 입력해주세요.'
        return
      }
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
        .then(() => {
          // console.log(res)
          this.$emit('close')
          this.$store.commit('SAVE_USER_EMAIL', this.email)

          this.email = null
          this.error = null
        })
        .catch((err) => {
          console.error(err)
          this.error = err.response.data.email[0]
        })
    },
    changePassword() {
      if (!this.newPassword1 || !this.newPassword2) {
        this.error = '새비밀번호를 입력해주세요.'
        return
      }
      if (this.newPassword1 != this.newPassword2) {
        this.error = '새 비밀번호가 일치하지 않습니다.'
        return
      }
      axiosAuth({
        method: 'post',
        url: `${this.axios_URL}/dj-rest-auth/password/change/`,
        data: {
          old_password: 'password',
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
          // console.error(err.response.data)

          this.error = err.response.data.new_password2

          this.newPassword1 = null
          this.newPassword2 = null
        })
    },
  },
}
</script>

<style></style>
