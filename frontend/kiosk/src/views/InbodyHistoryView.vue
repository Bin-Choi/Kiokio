<template>
  <div class="h-100 d-flex flex-column">
    <!-- BACK -->
    <div
      class="d-flex justify-content-between"
      style="font-size: 4vh; margin: 3vh; margin-bottom: 0"
    >
      <font-awesome-icon
        icon="fa-solid fa-circle-arrow-left"
        @click="$router.push({ name: 'inbody' })"
      />
      <font-awesome-icon
        icon="fa-solid fa-house"
        @click="$router.push({ name: 'index' })"
      />
    </div>

    <!-- PAGE TITLE -->
    <div id="title" class="w-75 title m-auto shadow">인바디 목록</div>

    <div style="font-size: 3vh">
      {{ student.grade }}학년 {{ student.room }}반 {{ student.name }}
    </div>

    <!-- INBODY HISTORY -->
    <div class="w-75 bg-white round m-auto shadow">
      <div id="scroll-box" class="container" style="padding: 2vh">
        <div class="row" style="font-weight: bold; font-size: 1.6vh">
          <p class="col">검사일</p>
          <p class="col">나이</p>
          <p class="col">키</p>
          <p class="col">체중</p>
          <p class="col">체지방률</p>
        </div>
        <inbody-history-item
          v-for="inbody in this.inbodyList"
          :key="inbody.pk"
          :inbody="inbody"
        />
      </div>
    </div>
    <div class="w-75 m-auto d-flex justify-content-between">
      <button
        class="orange-btn shadow w-50"
        style="padding: 1vh; margin-right: 1vh"
        @click="$router.push({ name: 'passwordUpdate' })"
      >
        비밀번호 변경
      </button>
      <button
        class="orange-btn shadow w-50"
        style="margin-left: 1vh"
        @click="$router.push({ name: 'inbodyCreate' })"
      >
        등록하기
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import InbodyHistoryItem from '../components/InbodyHistoryItem.vue'

export default {
  name: 'InbodyHistoryView',
  components: { InbodyHistoryItem },

  data() {
    return {
      inbodyList: null,
    }
  },
  computed: {
    axios_URL() {
      return this.$store.state.axios_URL
    },
    student() {
      return this.$store.state.student
    },
  },
  created() {
    axios({
      method: 'post',
      url: `${this.axios_URL}/students/${this.student.id}/inbody/list/`,
      data: {
        password: this.student.password,
      },
    })
      .then((res) => {
        this.inbodyList = res.data
      })

      .catch((err) => {
        console.log(err)
      })
  },
}
</script>

<style></style>
