<template>
  <div class="d-flex flex-column">
    <div class="d-flex justify-content-between">
      <div
        class="d-flex"
        @click="$router.push({ name: 'admin' })"
        style="font-size: 4vh; cursor: pointer">
        <font-awesome-icon icon="fa-solid fa-circle-arrow-left" />
      </div>
      <button
        class="green-btn"
        @click="$router.push({ name: 'studentCreate' })">
        + 학생 등록
      </button>
    </div>
    <div class="d-flex justify-content-between">
      <div class="d-flex">
        <div>학년</div>
        <input
          type="number"
          class="student-search-form"
          ref="grade"
          v-model.trim="grade"
          @keyup.enter="$refs.room.focus()" />
        <div>반</div>
        <input
          type="number"
          class="student-search-form"
          ref="room"
          v-model.trim="room" />
        <button class="blue-btn" @click="searchByClass">학급 조회</button>
      </div>
      <div class="d-flex">
        <div>이름</div>
        <input
          type="text"
          class="student-search-form"
          ref="name"
          v-model.trim="name" />
        <button class="blue-btn" @click="searchByName">이름 조회</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'StudentHeader',
  data() {
    return {
      grade: null,
      room: null,
      name: null,
    }
  },
  methods: {
    searchByClass() {
      if (!this.grade || !this.room) {
        alert('학년, 반을 모두 입력해주세요')
        return
      }
      this.name = null
      this.$emit('search-by-class', this.grade, this.room)
    },
    searchByName() {
      if (!this.name) {
        alert('이름을 입력해주세요')
        return
      }
      this.grade = null
      this.room = null
      this.$emit('search-by-name', this.name)
    },
  },
}
</script>

<style scoped>
.student-search-form {
  background-color: white;
  width: 10vw;
  height: 4vh;
  border-radius: 1vh;
}
</style>
