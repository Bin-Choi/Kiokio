<template>
  <div class="d-flex justify-content-between w-100">
    <div @click="$router.push({ name: 'admin' })" style="cursor: pointer">
      <font-awesome-icon icon="fa-solid fa-house" />
      <span>관리자 홈</span>
    </div>
    <div @click="$store.dispatch('logout')" style="cursor: pointer">
      <font-awesome-icon icon="fa-solid fa-user" />
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
