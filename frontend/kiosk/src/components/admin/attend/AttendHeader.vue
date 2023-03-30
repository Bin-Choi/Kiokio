<template>
  <div style="margin-bottom: 1vh">
    <div
      class="d-flex justify-content-between"
      style="margin: 0 0 2vh 0; font-size: 3vh"
    >
      <IconButton :icon="'fa-solid fa-circle-arrow-left'" :onClick="goAdmin" />

      <div>출결 관리</div>

      <IconButton
        :class="{ hidden: !students }"
        :icon="'fa-solid fa-table'"
        :text="'다운로드'"
        :onClick="() => $emit('download-excel')"
      />
    </div>
  </div>
</template>

<script>
import IconButton from '@/components/admin/common/IconButton.vue'

export default {
  name: 'AttendHeader',
  components: {
    IconButton,
  },
  computed: {
    students() {
      return this.$store.state.students
    },
  },
  methods: {
    goAdmin() {
      this.$router.push({ name: 'admin' })
      this.$store.commit('GET_STUDENTS', [])
    },
  },
}
</script>

<style scoped>
.hidden {
  visibility: hidden;
}
</style>
