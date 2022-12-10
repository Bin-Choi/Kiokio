<template>
  <div class="modal-bg h-100 d-flex flex-column justify-content-between">
    <div class="h-50 modal-content rounded shadow" style="padding: 2vh">
      <!-- CLOSE -->
      <font-awesome-icon
        icon="fa-solid fa-circle-xmark"
        class="align-self-end"
        style="font-size: 3.5vh; margin: 0 3vh"
        @click="$emit('close-modal')"
      />

      <div
        id="title"
        class="w-75 bg-primary rounded text-light shadow"
        style="font-size: 4vh; margin: auto; margin-bottom: 2vh; padding: 1vh"
      >
        비밀번호 입력
      </div>
      <!-- PASSWORD INPUT -->
      <div
        class="w-75 h-50 m-auto rounded shadow bg-light d-flex flex-column justify-content-evenly align-items-center"
      >
        <input
          type="password"
          maxlength="4"
          minlength="4"
          ref="password"
          @focus="focusChange"
          class="w-50 rounded"
          style="font-size: 3vh; padding: 1vh"
        />

        <button
          type="button"
          class="w-25 btn btn-primary shadow"
          style="font-size: 3vh"
          @click="submit"
        >
          확인
        </button>
      </div>
    </div>
    <!-- KEYPAD -->
    <TheKeypad @input="input" @del="del" class="w-100" />
  </div>
</template>

<script>
import TheKeypad from '@/components/TheKeypad.vue'

import axios from 'axios'

export default {
  name: 'ModalPwView',
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
    pk() {
      return this.$store.state.student.pk
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
        return
      }

      axios({
        method: 'post',
        url: `${this.axios_URL}/students/inbody/login/`,
        data: {
          password: this.$refs.password.value,
          pk: this.pk,
        },
      })
        .then((res) => {
          this.$store.commit('SAVE_PW_TOKEN', res.data.password)
          this.$router.push({ name: 'inbodyHistory' })
        })

        .catch(() => {
          alert('비밀번호가 틀렸습니다.')
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
  width: 90%;
  height: 50%;
  top: 5%;
}

input {
  background-color: #2b64aa1e;
}
</style>
