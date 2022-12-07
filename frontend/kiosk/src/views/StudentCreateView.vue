<template>
  <div
    class="d-flex flex-column align-items-center"
    style="width: 100vw; height: 100vh; padding: 7vh">
    <div class="d-flex justify-content-between w-100">
      <div @click="$router.push({ name: 'index' })" style="cursor: pointer">
        <font-awesome-icon icon="fa-solid fa-house" />
        <span>키오스크 홈</span>
      </div>
      <div @click="$store.dispatch('logout')" style="cursor: pointer">
        <font-awesome-icon icon="fa-solid fa-user" />
        <span>로그아웃</span>
      </div>
    </div>

    <div
      class="bg-secondary rounded shadow d-flex flex-column"
      style="width: 100%; height: 80vh; padding: 3vh; margin-top: 5vh">
      <div class="d-flex justify-content-between">
        <div>아래 항목 중 필터를 원하는 값만 입력하세요</div>
        <div
          class="student-add-btn"
          @click="$router.push({ name: 'studentCreate' })">
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
