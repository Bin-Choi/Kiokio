<template>
  <div
    class="d-flex flex-column align-items-center"
    style="width: 100vw; height: 100vh; padding: 7vh"
  >
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
      class="d-flex flex-column justify-content-around align-items-center w-100 h-100"
      style="padding-top: 15vh; padding-bottom: 15vh"
    >
      <div
        class="admin-view-button bg-light rounded shadow"
        @click="$router.push({ name: 'student' })"
      >
        학생관리
      </div>
      <div class="admin-view-button bg-light rounded shadow">출결관리</div>
      <div class="admin-view-button bg-light rounded shadow">인바디관리</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AdminView',
  methods: {},
}
</script>

<style scoped>
.admin-view-button {
  cursor: pointer;
  width: 40vw;
  height: 10vh;
  line-height: 10vh;
  font-size: 3vh;
}
</style>
