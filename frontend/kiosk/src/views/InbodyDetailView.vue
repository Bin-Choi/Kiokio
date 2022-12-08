<template>
  <div>
    <!-- BACK -->
    <div
      class="d-flex"
      @click="$router.go(-1)"
      style="font-size: 4.5vh; margin: 2.5vh; margin-bottom: 1vh"
    >
      <font-awesome-icon icon="fa-solid fa-circle-arrow-left" />
    </div>

    <div
      class="h-100 d-flex flex-column justify-content-between align-items-center"
      style="padding: 2vh 0"
    >
      <div
        class="w-75 bg-primary rounded text-light shadow"
        style="font-size: 5vh"
      >
        인바디 정보
      </div>

      <div style="font-size: 3vh">
        {{ student.grade }}학년 {{ student.room }}반 {{ student.name }}
      </div>

      <!-- INBODY CONTENT -->
      <inbody-detail />

      <!-- BUTTONS -->
      <div class="w-75 d-flex">
        <button
          type="button"
          class="btn btn-success shadow w-50"
          style="font-size: 2.5vh; margin: 0 1vh; padding: 1vh"
          @click="$router.push({ name: 'inbodyUpdate' })"
        >
          수정하기
        </button>
        <button
          type="button"
          class="btn btn-danger shadow w-50"
          style="font-size: 2.5vh; margin: 0 1vh; padding: 1vh"
          @click="del"
        >
          삭제하기
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import InbodyDetail from '@/components/InbodyDetail.vue'

import axios from 'axios'

export default {
  name: 'InbodyDetailView',
  components: {
    InbodyDetail,
  },
  computed: {
    student() {
      return this.$store.state.student
    },
    inbodyPk() {
      return this.$store.state.inbody.id
    },
    axios_URL() {
      return this.$store.state.axios_URL
    },
  },
  methods: {
    del() {
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          method: 'delete',
          url: `${this.axios_URL}/students/inbody/${this.inbodyPk}/`,
        })
          .then(() => {
            this.$router.push({ name: 'inbodyHistory' })
          })
          .catch((err) => {
            console.log(err)
          })
      }
    },
  },
}
</script>

<style></style>
