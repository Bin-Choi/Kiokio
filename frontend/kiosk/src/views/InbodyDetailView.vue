<template>
  <div class="pt-5">
    <div
      id="title"
      class="w-75 m-auto bg-primary rounded text-light p-1"
      style="font-size: 90px"
    >
      인바디 정보
    </div>

    <!-- INBODY DETAIL CONTENT -->
    <scroll-view> </scroll-view>

    <!-- BUTTONS -->
    <button
      type="button"
      class="btn btn-primary m-1"
      @click="$router.push({ name: 'inbodyForm' })"
    >
      인바디 등록하기
    </button>

    <button type="button" class="btn btn-primary m-1" @click="goList">
      지난 기록 조회
    </button>

    <div class="w-25 d-flex m-2 align-items-center" @click="$router.go(-1)">
      <font-awesome-icon icon="fa-solid fa-arrow-left" /> 뒤로가기
    </div>
  </div>
</template>

<script>
import ScrollView from "@/components/ScrollView.vue"

export default {
  name: "InbodyDetailView",
  components: {
    ScrollView,
  },
  methods: {},
}
</script>

<style scoped>
button {
  box-shadow: 0 7px 7px rgba(17, 61, 147, 0.987);
}
</style>
