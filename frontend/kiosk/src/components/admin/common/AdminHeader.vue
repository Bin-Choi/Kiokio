<template>
  <div
    class="d-flex justify-content-between w-100"
    style="min-width: 250px; max-width: 1310px"
  >
    <IconButton
      :class="{ hidden: $route.name == 'admin' }"
      :icon="'fa-solid fa-house'"
      :text="'홈'"
      :onClick="() => $router.push({ name: 'admin' })"
    />
    <div class="w-100 d-flex justify-content-end gap-4">
      <IconButton
        v-if="user.email"
        :icon="'fa-solid fa-envelope'"
        :text="'이메일 변경'"
        :onClick="() => $store.commit('TOGGLE_SHOW_CHANGE_EMAIL_MODAL', true)"
      />

      <IconButton
        :icon="'fa-solid fa-lock'"
        :text="'비밀번호 변경'"
        :onClick="
          () => $store.commit('TOGGLE_SHOW_CHANGE_PASSWORD_MODAL', true)
        "
      />

      <IconButton
        :icon="'fa-solid fa-user'"
        :text="'로그아웃'"
        :onClick="() => $store.dispatch('logout')"
      />
    </div>
  </div>
</template>

<script>
import IconButton from '@/components/admin/common/IconButton.vue'

export default {
  name: 'AdminHeader',
  components: {
    IconButton,
  },
  computed: {
    user() {
      return this.$store.state.user
    },
  },
}
</script>

<style>
.hidden {
  visibility: hidden;
}
</style>
