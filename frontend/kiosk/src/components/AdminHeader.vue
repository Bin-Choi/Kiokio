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
      v-if="user.email"
      @click="$store.commit('TOGGLE_SHOW_CHANGE_EMAIL_MODAL', true)"
      style="cursor: pointer">
      <font-awesome-icon icon="fa-solid fa-envelope" />
      <span>이메일 변경</span>
    </div>
    <div
      @click="$store.commit('TOGGLE_SHOW_CHANGE_PASSWORD_MODAL', true)"
      style="cursor: pointer">
      <font-awesome-icon icon="fa-solid fa-lock" />
      <span>비밀번호 변경</span>
    </div>
    <div @click="$store.dispatch('logout')" style="cursor: pointer">
      <font-awesome-icon icon="fa-solid fa-user" />
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
  computed: {
    user() {
      return this.$store.state.user
    },
  },
}
</script>

<style></style>
