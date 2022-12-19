<template>
  <div id="app" class="d-flex flex-column">
    <ChangeEmailModal
      v-if="showChangeEmailModal"
      @close="$store.commit('TOGGLE_SHOW_CHANGE_EMAIL_MODAL', false)"
    >
    </ChangeEmailModal>

    <ChangePasswordModal
      v-if="showChangePasswordModal"
      @close="$store.commit('TOGGLE_SHOW_CHANGE_PASSWORD_MODAL', false)"
    >
    </ChangePasswordModal>

    <LoginModal
      v-if="showLoginModal"
      @close="$store.commit('TOGGLE_SHOW_LOGIN_MODAL', false)"
    >
    </LoginModal>
    <router-view />
  </div>
</template>

<script>
import LoginModal from "@/components/LoginModal.vue"
import ChangePasswordModal from "@/components/ChangePasswordModal.vue"
import ChangeEmailModal from "@/components/ChangeEmailModal.vue"

export default {
  name: "AppView",
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

  background-color: #ffe8d299;
  font-family: "standard";
  font-size: 1.8vh;
}

table {
  width: 100%;
  table-layout: auto;
}

.title {
  font-size: 5vh;
  background-color: #ffa946;
  border-radius: 2.5vh;
  color: white;
}

.orange-btn {
  background-color: #ffa946;
  padding: 0.5vh 1vh;
  font-size: 3vh;
  color: white;
  border-radius: 1.5vh;
  border: none;
}

.round {
  border-radius: 2vh;
}

#scroll-box {
  height: 60vh;
  overflow: auto;
}

#scroll-box::-webkit-scrollbar {
  width: 1vh;
}
#scroll-box::-webkit-scrollbar-thumb {
  background-color: #ffa946;
  border-radius: 0.5vh;
}

#scroll-box::-webkit-scrollbar-corner {
  display: none;
}
</style>
