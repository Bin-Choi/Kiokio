<template>
  <div class="h-100 d-flex flex-column justify-content-between">
    <div
      id="title"
      class="w-75 m-auto bg-primary rounded text-light p-1"
      style="font-size: 90px"
    >
      지난 기록 조회
    </div>

    <scroll-view/>

    <!-- BUTTONS
    <button
      type="button"
      class="btn btn-primary m-1"
      @click="$router.push({ name: 'inbodyForm' })"
    >
      확인
    </button> -->

    <div class="d-flex m-5 align-items-center" style="font-size:2em;"
    @click="$router.go(-1)">
      <font-awesome-icon icon="fa-solid fa-arrow-left" /> 뒤로가기
    </div>
  </div>
</template>

<script>
import ScrollView from '@/components/ScrollView.vue'

export default {
  name: "InbodyHistoryView",
  components: {
    ScrollView,
  }
}
</script>

<style></style>
