<template>
  <div style="width: 100%; margin-bottom: 1vh; min-width: 410px">
    <font-awesome-icon
      icon="fa-solid fa-circle-arrow-left"
      @click="$router.go(-1)"
      style="font-size: 3vh; cursor: pointer"
      class="d-flex"
    />

    <div class="w-100 d-flex justify-content-end">
      <button
        v-if="!readyDelete"
        class="green-btn shadow-sm"
        @click="$emit('add-row')"
      >
        학생 추가
      </button>

      <button class="red-btn shadow-sm" @click="$emit('delete-row')">
        학생 삭제
      </button>

      <button
        v-if="!readyDelete"
        class="blue-btn shadow-sm"
        @click="$emit('create-student')"
      >
        저장
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "StudentCreateHeader",
  props: {
    readyDelete: Boolean,
  },
}
</script>

<style scoped>
button {
  margin: 0 0.5vh;
}
</style>
