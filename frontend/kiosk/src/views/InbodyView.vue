<template>
  <div id="inbody" class="h-100 d-flex flex-column justify-content-between">
    <!-- MODAL -->
    <modal-pw-view v-if="showModal" />

    <!-- BACK -->
    <div
      class="d-flex"
      @click="$router.go(-1)"
      style="font-size: 4.5vh; margin: 3vh; margin-bottom: 0"
    >
      <font-awesome-icon icon="fa-solid fa-circle-arrow-left" />
    </div>

    <div
      class="h-50 d-flex flex-column align-items-center justify-content-around"
    >
      <!-- PAGE TITLE -->
      <div
        v-if="!showModal"
        class="w-75 bg-primary rounded text-light shadow"
        style="font-size: 5vh"
      >
        인바디 등록/조회
      </div>

      <!-- INFO -->
      <info-view v-if="!showModal" />

      <div
        v-if="!showModal"
        class="d-flex align-items-center justify-content-center"
      >
        <!-- INPUT -->
        <input
          type="text"
          v-model.trim="num"
          maxlength="5"
          minlength="5"
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
    <TheKeypad @show-pw-modal="showModal = true" />
  </div>
</template>

<script>
import InfoView from '@/components/InfoView.vue'
import TheKeypad from '@/components/TheKeypad.vue'
import ModalPwView from '../components/ModalPwView.vue'

import axios from "axios"

export default {
  name: 'InbodyView',
  components: {
    InfoView,
    TheKeypad,
    ModalPwView,
  },
  data() {
    return {
      num: '',
      showModal: false,
    }
  },
  methods: {
    submit() {
      // CHECK INPUT FORM
      if (!this.num || this.num.length != 5) {
        alert('학년 반 번호를 정확히 입력해주세요')
        return false
      }

      const URL = 'http://127.0.0.1:8000'
      axios({
        method: 'get',
        url: `${URL}/students/inbody/`,
        data: {
          number: this.num,
        },
      })
        .then((res) => {
          this.$store.commit('STUDENT_INFO', res.data)
          this.showModal = true
        })

        .catch((err) => {
          alert('없는 번호입니다.')
          console.log(err)
        })

      this.num = ''
    },
  },
}
</script>

<style></style>
