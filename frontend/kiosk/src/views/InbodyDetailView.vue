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

      <div style="font-size: 3vh">0학년 0반 학생이름</div>

      <!-- INBODY CONTENT -->
      <inbody-detail />

      <!-- BUTTONS -->
      <div class="w-75 d-flex">
        <button
          type="button"
          class="btn btn-primary shadow w-50"
          style="font-size: 2.5vh; margin: 0 1vh; padding: 1.5vh"
          @click="$router.push({ name: 'inbodyForm' })"
        >
          인바디 등록
        </button>

        <button
          type="button"
          class="btn btn-primary shadow w-50"
          style="font-size: 2.5vh; margin: 0 1vh; padding: 1.5vh"
          @click="$router.push({ name: 'inbodyHistory' })"
        >
          지난기록 조회
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import InbodyDetail from '@/components/InbodyDetail.vue'

export default {
  name: 'InbodyDetailView',
  components: {
    InbodyDetail,
  },
}
</script>

<style></style>
