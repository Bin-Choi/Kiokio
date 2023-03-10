<template>
  <div class="d-flex flex-column" style="margin-bottom: 1vh; min-width: 550px">
    <div
      class="d-flex justify-content-between"
      style="margin: 0 0 2vh 0; font-size: 3vh"
    >
      <IconButton :icon="'fa-solid fa-circle-arrow-left'" :onClick="goAdmin" />

      <div>학생 관리</div>

      <IconButton
        :class="{ hidden: $route.name != 'student' || !students }"
        :icon="'fa-solid fa-table'"
        :text="'다운로드'"
        :onClick="() => $emit('download-excel')"
      />
    </div>
  </div>
</template>

<script>
import IconButton from '../common/IconButton.vue'

export default {
  name: 'StudentHeader',
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
