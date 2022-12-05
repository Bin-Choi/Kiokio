<template>
  <div class="h-100 d-flex flex-column justify-content-between">
    <div
      class="w-75 m-auto bg-primary rounded text-light p-1 shadow"
      style="font-size: 3em"
    >
      인바디 정보
    </div>

    <!-- INBODY DETAIL CONTENT -->
    <scroll-view> </scroll-view>

    <!-- BUTTONS -->
    <div class="w-75 d-flex justify-content-around m-auto">
      <button
        type="button"
        class="btn btn-primary shadow p-3" style="font-size: 1.5em;"
        @click="$router.push({ name: 'inbodyForm' })"
      >
        인바디 등록하기
      </button>

      <button
        type="button"
        class="btn btn-primary shadow p-3" style="font-size: 1.5em;"
        @click="$router.push({ name: 'inbodyHistory' })"
      >
        지난 기록 조회
      </button>
    </div>

    <!-- BACK -->
    <div class="d-flex m-5 align-items-center" style="font-size:2em;"
    @click="$router.go(-1)">
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

<style>

</style>
