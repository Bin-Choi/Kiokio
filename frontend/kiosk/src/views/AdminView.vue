<template>
  <div
    class="d-flex flex-column align-items-center"
    style="width: 100vw; height: 100vh; padding: 7vh">
    <AdminHeader />
    <div
      class="d-flex flex-column justify-content-around align-items-center w-100 h-100"
      style="padding-top: 15vh; padding-bottom: 15vh"
    >
      <div
        class="admin-view-button rounded shadow-sm"
        @click="$router.push({ name: 'student' })"
      >
        학생관리
      </div>
      <div
        class="admin-view-button rounded shadow-sm"
        @click="$router.push({ name: 'attendance' })">
        출결관리
      </div>
      <div class="admin-view-button rounded shadow-sm">인바디관리</div>
    </div>
  </div>
</template>

<script>
import AdminHeader from '@/components/AdminHeader.vue'

export default {
  name: 'AdminView',
  components: {
    AdminHeader,
  },
}
</script>

<style scoped>
.admin-view-button {
  background-color: #2b64aa1e;
  cursor: pointer;
  width: 40vw;
  height: 10vh;
  line-height: 10vh;
  font-size: 3vh;
}
</style>
