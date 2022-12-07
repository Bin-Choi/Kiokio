<template>
  <div class="h-100 d-flex flex-column">
    <!-- BACK -->
    <div
      class="d-flex"
      @click="$router.go(-1)"
      style="font-size: 4.5vh; margin: 3vh; margin-bottom: 0"
    >
      <font-awesome-icon icon="fa-solid fa-circle-arrow-left" />
    </div>

    <!-- PAGE TITLE -->
    <div
      id="title"
      class="w-75 m-auto mb-0 bg-primary rounded text-light shadow"
      style="font-size: 5vh"
    >
      지난 기록 조회
    </div>

    <!-- INBODY HISTORY -->
    <div class="w-75 bg-light rounded m-auto shadow" style="padding: 2.5vh 2vh">
      <div id="scroll-box" class="container">
        <div class="row" style="font-weight: bold">
          <p class="col">검사 날짜</p>
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
    pk() {
      return this.$store.state.studentPk
    },
  },
  created() {
    axios({
      method: 'get',
      url: `${this.axios_URL}/students/${this.pk}/inbody/list/`,
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
