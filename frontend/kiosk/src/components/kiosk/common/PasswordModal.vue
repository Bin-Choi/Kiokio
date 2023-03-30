<template>
  <div class="modal-bg h-100 d-flex flex-column justify-content-between">
    <div class="modal-content bg-white shadow">
      <!-- CLOSE -->
      <font-awesome-icon
        icon="fa-solid fa-circle-xmark"
        class="align-self-end"
        style="font-size: 4vh; margin: 3vh 3vh 0 0"
        @click="$emit('close-modal')"
      />

      <div class="w-75 title shadow m-auto">비밀번호 입력</div>
      <!-- PASSWORD INPUT -->

      <input
        type="password"
        maxlength="4"
        minlength="4"
        ref="password"
        @focus="focusChange"
        class="w-50 shadow-sm m-auto"
      />

      <button class="w-25 orange-btn shadow m-auto" @click="submit">
        확인
      </button>
    </div>
    <!-- KEYPAD -->
    <TheKeypad
      @input="input"
      @del="del"
      style="width: 100%; margin-bottom: 5vh"
    />
  </div>
</template>

<script>
// import TheKeypad from "@/components/TheKeypad.vue"
import TheKeypad from './TheKeypad.vue'

import axios from 'axios'

// const pwKey = b"ABCD"

export default {
  name: 'PasswordModal',
  components: {
    TheKeypad,
  },
  props: {
    num: String,
  },
  computed: {
    axios_URL() {
      return this.$store.state.axios_URL
    },
  },
  mounted() {
    this.$refs.password.focus()
  },
  methods: {
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
      // 비밀번호 xor 연산하여 간이 암호화

      axios({
        method: 'post',
        url: `${this.axios_URL}/students/${this.num}/inbody/`,
        data: {
          password: this.$refs.password.value,
        },
      })
        .then((res) => {
          this.$store.commit('SAVE_ID_PASSWORD', res.data)
          this.$router.push({ name: 'inbodyHistory' })
        })

        .catch(() => {
          alert('비밀번호가 틀렸습니다.')
          this.$refs.password.value = null
          this.$refs.password.focus()
        })
    },
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
  },
}
</script>

<style scoped>
.modal-bg {
  display: flex;
  align-items: center;
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
}

.modal-content {
  width: 85%;
  height: 45%;
  top: 13%;
}

input {
  border-radius: 2vh;
  border: 0.5vh solid #ffa946;
  background-color: #ffe8d299;
  font-size: 3vh;
  padding: 1vh;
}
</style>
