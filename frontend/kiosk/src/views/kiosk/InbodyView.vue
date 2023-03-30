<template>
  <div
    id="inbody"
    class="d-flex flex-column justify-content-between"
    style="height: 100vh"
  >
    <!-- MODAL -->
    <PasswordModal
      v-if="showModal"
      :num="this.$refs.num.value"
      @close-modal="showModal = false"
    />

    <kiosk-header />

    <div
      v-if="!showModal"
      class="h-50 d-flex flex-column align-items-center justify-content-around"
    >
      <!-- PAGE TITLE -->
      <div class="title w-75 shadow">인바디</div>

      <!-- INFO -->
      <TheNumGuide />

      <div class="d-flex align-items-center justify-content-center">
        <!-- INPUT -->
        <input
          type="text"
          maxlength="5"
          minlength="5"
          ref="num"
          @focus="focusChange"
          class="w-50 shadow-sm round"
          style="padding: 1vh; margin-right: 2vh; font-size: 3vh"
        />

        <!-- SUBMIT -->
        <button class="orange-btn shadow" @click="submit">확인</button>
      </div>
    </div>

    <!-- KEYPAD -->
    <TheKeypad
      v-if="!showModal"
      @show-pw-modal="showModal = true"
      @input="input"
      @del="del"
      style="margin-bottom: 5vh"
    />
  </div>
</template>

<script>
// import TheNumGuide from '@/components/kiosk/common/TheNumGuide.vue'
// import TheKeypad from '@/components/TheKeypad.vue'
// import PasswordModal from '../../../components/PasswordModal.vue'
// import KioskHeader from '@/components/KioskHeader.vue'

import TheNumGuide from '@/components/kiosk/common/TheNumGuide.vue'
import TheKeypad from '@/components/kiosk/common/TheKeypad.vue'
import PasswordModal from '@/components/kiosk/common/PasswordModal.vue'
import KioskHeader from '@/components/kiosk/common/KioskHeader.vue'

import axios from 'axios'

export default {
  name: 'InbodyView',
  components: {
    TheNumGuide,
    TheKeypad,
    PasswordModal,
    KioskHeader,
  },
  data() {
    return {
      showModal: false,
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
        url: `${this.axios_URL}/students/${this.$refs.num.value}/inbody/`,
      })
        .then((res) => {
          this.$store.commit('STUDENT_INFO', res.data)
          this.showModal = true
        })

        .catch(() => {
          alert('없는 학생입니다.')
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

<style></style>
