<template>
  <div class="pt-5">
    <div
      id="title"
      class="w-75 m-auto bg-primary rounded text-light p-1"
      style="font-size: 90px"
    >
      지난 기록 조회
    </div>
    <div class="w-75 bg-light rounded m-auto my-3 py-3 px-2"></div>
    <!-- BUTTONS
    <button
      type="button"
      class="btn btn-primary m-1"
      @click="$router.push({ name: 'inbodyForm' })"
    >
      확인
    </button> -->
    <div class="w-25 d-flex m-2 align-items-center" @click="$router.go(-1)">
      <font-awesome-icon icon="fa-solid fa-arrow-left" /> 뒤로가기
    </div>
  </div>
</template>

<script>
export default {
  name: "InbodyListView",
}
</script>

<style></style>
