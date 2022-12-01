<template>
  <div>
    <div
      id="title"
      class="w-75 m-auto bg-primary rounded text-light p-1"
      style="font-size: 90px"
    >
      인바디 정보
    </div>

    <div id="info-box" class="w-75 bg-light m-auto p-2 mt-3 rounded">
      <div class="font-weight-bold">0 학년 0 반 이름 000</div>
    </div>
    <InbodyDetail></InbodyDetail>
    <div class="d-flex flex-column w-50">
      <button
        type="button"
        class="btn btn-primary mb-2"
        @click="$router.push('inbodyForm')"
      >
        인바디 등록하기
      </button>
      <!-- <button type="button" class="btn btn-primary" @click="goList">
        지난 기록 조회
      </button> -->
    </div>
  </div>
</template>

<script>
import InbodyDetail from "../components/InbodyDetail.vue"

export default {
  name: "InbodyDetailView",
  components: {
    InbodyDetail,
  },
  methods: {},
}
</script>

<style></style>
