<template>
  <div class="h-100 d-flex flex-column justify-content-between">
    <!-- MODAL -->
    <modal-view
      v-if="showModal"
      @close-modal="showModal = false"
      :student="this.student"
    />

    <!-- BACK -->
    <div
      class="d-flex justify-content-between"
      style="font-size: 4.5vh; margin: 3vh; margin-bottom: 0"
    >
      <font-awesome-icon
        icon="fa-solid fa-circle-arrow-left"
        @click="$router.go(-1)"
      />
      <font-awesome-icon
        icon="fa-solid fa-house"
        @click="$router.push({ name: 'index' })"
      />
    </div>

    <div
      class="h-50 d-flex flex-column align-items-center justify-content-around"
    >
      <!-- PAGE TITLE -->
      <div
        class="w-75 bg-primary rounded text-light shadow"
        style="font-size: 5vh"
      >
        출석체크
      </div>

      <!-- INFO -->
      <info-view />

      <div class="d-flex align-items-center justify-content-center">
        <!-- INPUT -->
        <input
          type="text"
          maxlength="5"
          minlength="5"
          ref="num"
          @focus="focusChange"
          class="w-50 rounded bg-light"
          style="padding: 1vh; margin-right: 2vh; font-size: 3vh"
        />

        <!-- SUBMIT -->
        <button
          type="button"
          class="btn btn-primary shadow"
          style="font-size: 3vh"
          @click="submit"
        >
          확인
        </button>
      </div>
    </div>

    <!-- KEYPAD -->
    <TheKeypad @input="input" @del="del" />
  </div>
</template>

<script>
import InfoView from '@/components/InfoView.vue'
import TheKeypad from '@/components/TheKeypad.vue'
import ModalView from '@/components/ModalView.vue'

import axios from 'axios'

export default {
  name: 'AttendView',
  components: {
    InfoView,
    ModalView,
    TheKeypad,
  },
  data() {
    return {
      student: null,
      showModal: false,
      focusElem: null,
    }
  },
  computed: {
    axios_URL() {
      return this.$store.state.axios_URL
    },
  },
  mounted() {
    this.$refs.num.focus()
  },
  methods: {
    submit() {
      // Num validation
      const regInt = /^[0-9]*$/

      if (
        !regInt.test(this.$refs.num.value) ||
        this.$refs.num.value.length != 5
      ) {
        alert('학년 반 번호를 정확히 입력해주세요')

        this.$refs.num.value = null
        this.$refs.num.focus()

        return
      }
      axios({
        method: 'get',
        url: `${this.axios_URL}/students/${this.$refs.num.value}/attendance/`,
        data: {
          num: this.$refs.num.value,
        },
      })
        .then((res) => {
          this.student = res.data
          this.showModal = true
          this.$refs.num.value = ''
        })

        .catch(() => {
          alert('없는 번호입니다.')
          this.$refs.num.value = null
          this.$refs.num.focus()
        })
    },
    focusChange(event) {
      this.focusElem = event.target
    },
    input(value) {
      if (this.focusElem.value.length < 5) {
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

<style>
input {
  text-align: center;
  border: none;
}

input:focus {
  outline: none;
}
</style>
