<template>
  <div id="inbody" class="h-100 d-flex flex-column justify-content-between">
    <!-- MODAL -->
    <modal-pw-view
      v-if="showModal"
      :num="this.$refs.num.value"
      @close-modal="showModal = false"
    />

    <!-- BACK -->
    <div
      v-if="!showModal"
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
        v-if="!showModal"
        class="w-75 bg-primary rounded text-light shadow"
        style="font-size: 5vh"
      >
        인바디
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
          maxlength="5"
          minlength="5"
          ref="num"
          @focus="focusChange"
          @input="(event) => (text = event.target.value)"
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
    <TheKeypad
      v-if="!showModal"
      @show-pw-modal="showModal = true"
      @input="input"
      @del="del"
    />
  </div>
</template>

<script>
import InfoView from '@/components/InfoView.vue'
import TheKeypad from '@/components/TheKeypad.vue'
import ModalPwView from '../components/ModalPwView.vue'

import axios from 'axios'

export default {
  name: 'InbodyView',
  components: {
    InfoView,
    TheKeypad,
    ModalPwView,
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
    // Submit Event
    submit() {
      // Check the input length
      if (!this.$refs.num.value || this.$refs.num.value.length != 5) {
        alert('학년 반 번호를 정확히 입력해주세요')
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

        .catch((err) => {
          alert('없는 번호입니다.')
          console.log(err)
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
