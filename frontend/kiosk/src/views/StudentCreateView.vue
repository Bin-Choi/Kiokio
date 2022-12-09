<template>
  <div
    class="bg-white d-flex flex-column align-items-center"
    style="width: 100vw; height: 100vh; padding: 7vh"
  >
    <div class="d-flex justify-content-between w-100">
      <div
        @click="$store.dispatch('logout')"
        style="cursor: pointer"
        class="d-flex flex-column"
      >
        <font-awesome-icon icon="fa-solid fa-user" style="font-size: 3vh" />
        <span>로그아웃</span>
      </div>
      <div
        @click="$router.push({ name: 'index' })"
        class="d-flex flex-column"
        style="cursor: pointer"
      >
        <font-awesome-icon icon="fa-solid fa-house" style="font-size: 3vh" />
        <span>키오스크 홈</span>
      </div>
    </div>

    <div
      class="w-75 rounded shadow-sm d-flex flex-column"
      style="
        height: 80vh;
        padding: 3vh;
        margin-top: 5vh;
        border: 0.5vh solid #2b64aa1e;
      "
    >
      <div class="d-flex justify-content-between">
        <div>아래 항목 중 필터를 원하는 값만 입력하세요</div>
        <div
          class="btn btn-primary rounded shadow-sm font-weight-bold"
          @click="$router.push({ name: 'studentCreate' })"
        >
          + 학생 추가
        </div>
      </div>
      <div></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'StudentCreateView',
  methods: {},
}
</script>

<style scoped></style>
