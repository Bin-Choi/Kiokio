<template>
  <div
    class="h-100 d-flex flex-column align-items-center justify-content-between">
    <!-- BACK -->
    <div
      class="w-100 d-flex justify-content-between"
      style="font-size: 4.5vh; margin: 1.5vh; margin-bottom: 0; padding: 2.2vh">
      <font-awesome-icon
        icon="fa-solid fa-circle-arrow-left"
        @click="$router.go(-1)" />
      <font-awesome-icon
        icon="fa-solid fa-house"
        @click="$router.push({ name: 'index' })" />
    </div>

    <!-- PAGE TITLE -->
    <div
      class="w-75 bg-primary rounded text-light shadow"
      style="font-size: 5vh">
      비밀번호 변경
    </div>

    <!-- CONTENT -->
    <div
      class="w-75 rounded shadow bg-light d-flex flex-column align-items-center jusity-content-between"
      style="padding: 2.5vh 0; font-size: 2.5vh">
      <div>
        <div>기존 비밀번호</div>
        <input
          type="password"
          maxlength="4"
          minlength="4"
          ref="password"
          @focus="focusChange"
          class="rounded shadow-sm" />
      </div>

      <div>
        <div>새 비밀번호</div>
        <input
          type="password"
          maxlength="4"
          minlength="4"
          ref="newPassword"
          @focus="focusChange"
          class="rounded shadow-sm" />
      </div>

      <div>
        <div>비밀번호 확인</div>
        <input
          type="password"
          maxlength="4"
          minlength="4"
          ref="confirmPassword"
          @focus="focusChange"
          class="rounded shadow-sm" />
      </div>
      <button
        type="button"
        class="w-25 btn btn-primary shadow"
        style="font-size: 3vh; margin-top: 1vh"
        @click="submit">
        확인
      </button>
    </div>

    <!-- KEYPAD -->
    <the-keypad class="w-100 align-self-end" @input="input" @del="del" />
  </div>
</template>

<script>
import TheKeypad from '../components/TheKeypad.vue'

export default {
  components: { TheKeypad },
  name: 'PasswordUpdateView',
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
        alert('비밀번호를 정확히 입력해주세요')
        this.$refs.password.value = null
        this.$refs.password.focus()
        return
      }

      if (
        !regInt.test(this.$refs.newPassword.value) ||
        this.$refs.newPassword.value.length != 4
      ) {
        alert('비밀번호는 숫자 네자리로 설정해주세요')
        this.$refs.newPassword.value = null
        this.$refs.newPassword.focus()
        return
      }

      if (this.$refs.newPassword.value != this.$refs.confirmPassword.value) {
        alert('비밀번호가 일치하지 않습니다')
        this.$refs.confirmPassword.value = null
        this.$refs.confirmPassword.focus()
        return
      }
    },
  },
  mounted() {
    this.$refs.password.focus()
  },
}
</script>

<style scoped>
input {
  background-color: #2b64aa1e;
  width: 60%;
  padding: 0.7vh;
  margin-bottom: 1vh;
}
</style>
