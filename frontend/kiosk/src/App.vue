<template>
  <div id="app" class="d-flex flex-column">
    <ChangeEmailModal
      v-if="showChangeEmailModal"
      @close="$store.commit('TOGGLE_SHOW_CHANGE_EMAIL_MODAL', false)">
    </ChangeEmailModal>
    <ChangePasswordModal
      v-if="showChangePasswordModal"
      @close="$store.commit('TOGGLE_SHOW_CHANGE_PASSWORD_MODAL', false)">
    </ChangePasswordModal>
    <LoginModal
      v-if="showLoginModal"
      @close="$store.commit('TOGGLE_SHOW_LOGIN_MODAL', false)">
    </LoginModal>
    <router-view />
  </div>
</template>

<script>
import LoginModal from '@/components/LoginModal.vue'
import ChangePasswordModal from '@/components/ChangePasswordModal.vue'
import ChangeEmailModal from '@/components/ChangeEmailModal.vue'

export default {
  name: 'AppView',
  components: {
    LoginModal,
    ChangePasswordModal,
    ChangeEmailModal,
  },
  computed: {
    showLoginModal() {
      return this.$store.state.showLoginModal
    },
    showChangePasswordModal() {
      return this.$store.state.showChangePasswordModal
    },
    showChangeEmailModal() {
      return this.$store.state.showChangeEmailModal
    },
  },
}
</script>

<style>
#app {
  height: 100vh;
  text-align: center;
  background-color: #2b64aa1e;
}
</style>
