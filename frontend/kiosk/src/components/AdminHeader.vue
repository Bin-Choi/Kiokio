<template>
  <div class="d-flex justify-content-between w-100">
    <div @click="$router.push({ name: 'admin' })" style="cursor: pointer">
      <font-awesome-icon
        icon="fa-solid fa-house"
        class="d-flex flex-column m-auto"
        style="font-size: 3vh"
      />
      <span>관리자 홈</span>
    </div>
    <div
      @click="$store.dispatch('logout')"
      class="d-flex flex-column"
      style="cursor: pointer"
    >
      <font-awesome-icon icon="fa-solid fa-user" style="font-size: 3vh" />
      <span>로그아웃</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AdminHeader',
}
</script>

<style></style>
