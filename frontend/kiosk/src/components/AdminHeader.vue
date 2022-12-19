<template>
  <div class="d-flex justify-content-between w-100" style="min-width: 250px">
    <div
      :class="{ hidden: $route.name == 'admin' }"
      @click="$router.push({ name: 'admin' })"
      style="cursor: pointer"
    >
      <font-awesome-icon
        icon="fa-solid fa-house"
        class="d-flex flex-column m-auto icon"
      />
      <div>홈</div>
    </div>
    <div class="w-100 d-flex justify-content-end">
      <div
        v-if="user.email"
        @click="$store.commit('TOGGLE_SHOW_CHANGE_EMAIL_MODAL', true)"
        style="cursor: pointer"
      >
        <font-awesome-icon icon="fa-solid fa-envelope" class="icon" />
        <div>이메일 변경</div>
      </div>

      <div
        @click="$store.commit('TOGGLE_SHOW_CHANGE_PASSWORD_MODAL', true)"
        style="cursor: pointer; margin-left: 2vw; margin-right: 2vw"
      >
        <font-awesome-icon icon="fa-solid fa-lock" class="icon" />
        <div>비밀번호 변경</div>
      </div>

      <div @click="$store.dispatch('logout')" style="cursor: pointer">
        <font-awesome-icon icon="fa-solid fa-user" class="icon" />
        <div>로그아웃</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AdminHeader",
  computed: {
    user() {
      return this.$store.state.user
    },
  },
}
</script>

<style>
.icon {
  font-size: 2.5vh;
}
.hidden {
  visibility: hidden;
}
</style>
