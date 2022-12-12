<template>
  <div class="d-flex flex-column" style="margin-bottom: 1vh">
    <div
      class="d-flex justify-content-between"
      style="margin: 0 0 2vh 0; font-size: 3vh"
    >
      <font-awesome-icon
        icon="fa-solid fa-circle-arrow-left"
        @click="$router.push({ name: 'admin' })"
        style="cursor: pointer"
      />
      <div>인바디 관리</div>
      <div></div>
    </div>
    <div class="d-flex justify-content-between">
      <div>
        <span>학년</span>
        <input
          type="number"
          class="student-search-form"
          ref="grade"
          v-model.trim="grade"
          @keyup.enter="$refs.room.focus()"
        />
        <span>반</span>
        <input
          type="number"
          class="student-search-form"
          ref="room"
          v-model.trim="room"
        />
        <button class="blue-btn shadow-sm" @click="searchByClass">
          학급 조회
        </button>
      </div>
      <div>
        <span>이름</span>
        <input
          type="text"
          class="student-search-form"
          ref="name"
          v-model.trim="name"
        />
        <button class="blue-btn shadow-sm" @click="searchByName">
          이름 조회
        </button>
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

<style></style>
