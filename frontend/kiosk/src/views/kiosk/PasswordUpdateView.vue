<template>
  <div
    class="h-100 d-flex flex-column align-items-center justify-content-between"
  >
    <!-- BACK -->
    <div
      class="w-100 d-flex justify-content-between"
      style="font-size: 4vh; margin: 1.5vh; margin-bottom: 0; padding: 2.2vh"
    >
      <font-awesome-icon
        icon="fa-solid fa-circle-arrow-left"
        @click="$router.push({ name: 'inbodyHistory' })"
      />
      <font-awesome-icon
        icon="fa-solid fa-house"
        @click="$router.push({ name: 'index' })"
      />
    </div>

    <!-- PAGE TITLE -->
    <div class="w-75 title shadow">비밀번호 변경</div>

    <!-- CONTENT -->
    <div
      class="w-75 round shadow bg-white d-flex flex-column align-items-center jusity-content-between"
      style="padding: 2.5vh 0; font-size: 2.5vh"
    >
      <div>
        <div>기존 비밀번호</div>
        <input
          type="password"
          maxlength="4"
          minlength="4"
          ref="password"
          @focus="focusChange"
          class="shadow-sm"
        />
      </div>

      <div>
        <div>새 비밀번호</div>
        <input
          type="password"
          maxlength="4"
          minlength="4"
          ref="newPassword"
          @focus="focusChange"
          class="shadow-sm"
        />
      </div>

      <div>
        <div>비밀번호 확인</div>
        <input
          type="password"
          maxlength="4"
          minlength="4"
          ref="confirmPassword"
          @focus="focusChange"
          class="shadow-sm"
        />
      </div>
      <button
        class="w-25 orange-btn shadow"
        style="margin-top: 1vh"
        @click="submit"
      >
        확인
      </button>
    </div>

    <!-- KEYPAD -->
    <the-keypad class="w-100 align-self-end" @input="input" @del="del" />
  </div>
</template>

<script>
// import TheKeypad from '../components/TheKeypad.vue'
import TheKeypad from '@/components/kiosk/common/TheKeypad.vue'
import axios from 'axios'

export default {
  components: { TheKeypad },
  name: 'PasswordUpdateView',
  computed: {
    axios_URL() {
      return this.$store.state.axios_URL
    },
    student() {
      return this.$store.state.student
    },
  },
  methods: {
    focusChange(event) {
      this.focusElem = event.target
    },
    input(value) {
      if (this.focusElem.value.length < 4) {
        this.focusElem.value += value
      }
    },
    del() {
      if (this.focusElem.value.length > 0) {
        this.focusElem.value = this.focusElem.value.slice(0, -1)
      }
    },
    submit() {
      // Password validation
      const regInt = /^[0-9]*$/

      if (
        !regInt.test(this.$refs.password.value) ||
        this.$refs.password.value.length != 4
      ) {
        alert('비밀번호를 정확히 입력해주세요.')
        this.$refs.password.value = null
        this.$refs.password.focus()
        return
      }

      if (
        !regInt.test(this.$refs.newPassword.value) ||
        this.$refs.newPassword.value.length != 4
      ) {
        alert('비밀번호는 숫자 네자리로 설정해주세요.')
        this.$refs.newPassword.value = null
        this.$refs.newPassword.focus()
        return
      }

      if (this.$refs.newPassword.value != this.$refs.confirmPassword.value) {
        alert('새 비밀번호가 일치하지 않습니다.')
        this.$refs.confirmPassword.value = null
        this.$refs.confirmPassword.focus()
        return
      }

      axios({
        method: 'put',
        url: `${this.axios_URL}/students/${this.student.id}/password/`,
        data: {
          password: this.student.password,
          currentPassword: this.$refs.password.value,
          newPassword: this.$refs.newPassword.value,
        },
      })
        .then((res) => {
          alert('비밀번호가 변경되었습니다.')
          this.$store.commit('SAVE_ID_PASSWORD', res.data)
          this.$router.push({ name: 'inbodyHistory' })
        })

        .catch((err) => {
          const {
            response: { status },
          } = err
          if (status === 400) {
            alert('기존 비밀번호가 틀렸습니다.')
          } else if (status === 401) {
            alert('다시 로그인해주세요')
            this.$router.push({ name: 'inbody' })
          }
        })
    },
  },
  mounted() {
    this.$refs.password.focus()
  },
}
</script>

<style scoped>
input {
  border-radius: 1vh;
  border: 0.3vh solid #ffa946;
  background-color: #ffe8d299;
  width: 60%;
  padding: 0.7vh;
  margin-bottom: 1vh;
}
</style>
