<template>
  <div class="d-flex flex-column" style="margin-bottom: 1vh; min-width: 710px">
    <div
      class="d-flex justify-content-between"
      style="margin: 0 0 2vh 0; font-size: 3vh">
      <font-awesome-icon
        icon="fa-solid fa-circle-arrow-left"
        @click="$router.push({ name: 'admin' })"
        style="cursor: pointer" />
      <div>인바디 관리</div>
      <div :class="{ hidden: mode !== 'R' || !inbodies }">
        <font-awesome-icon
          icon="fa-solid fa-table"
          @click="$emit('download-excel')"
          style="font-size: 3vh; cursor: pointer" />
        <div style="font-size: 1.5vh">다운로드</div>
      </div>
    </div>
    <div class="d-flex justify-content-between">
      <div>
        <input
          type="date"
          class="student-search-form"
          style="width: 13vh"
          ref="date"
          v-model="date" />
      </div>
      <div>
        <span>학년</span>
        <input
          type="number"
          min="1"
          class="student-search-form"
          ref="grade"
          v-model.trim="grade"
          @keyup.enter="$refs.room.focus()" />
        <span>반</span>
        <input
          type="number"
          min="1"
          class="student-search-form"
          ref="room"
          v-model.trim="room"
          @keyup.enter="searchByClass" />
        <button class="blue-btn shadow-sm" @click="searchByClass">
          학급 조회
        </button>
        <span style="margin-left: 3vh">이름</span>
        <input
          type="text"
          class="student-search-form"
          ref="name"
          v-model.trim="name"
          @keyup.enter="searchByName" />
        <button class="blue-btn shadow-sm" @click="searchByName">
          이름 조회
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AdminInbodyDateHeader',
  props: {
    inbodies: Array,
    mode: String,
  },
  data() {
    return {
      date: null,
      grade: null,
      room: null,
      name: null,
    }
  },
  methods: {
    searchByClass() {
      const regDate = /^\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$/
      if (!regDate.test(this.date)) {
        alert('날짜를 선택해주세요')
        return
      }
      if (!this.grade || !this.room) {
        alert('학년, 반을 모두 입력해주세요')
        return
      }
      //학년 검사
      const regGrade = /^[1-9]$/
      if (!regGrade.test(this.grade)) {
        alert('학년은 1~9사이의 숫자로 입력하세요')
        return
      }
      //반 검사
      const regRoom = /^[1-9]$|^[1-9]{1}[0-9]{1}$/
      if (!regRoom.test(this.room)) {
        alert('반은 1~99사이의 숫자로 입력하세요')
        return
      }
      this.name = null
      this.$emit('search-by-class', this.date, this.grade, this.room)
    },
    searchByName() {
      const regDate = /^\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$/
      if (!regDate.test(this.date)) {
        alert('날짜를 선택해주세요')
        return
      }
      if (!this.name) {
        alert('이름을 입력해주세요')
        return
      }
      const regName = /^[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]{2,}$/
      if (!regName.test(this.name)) {
        alert('이름은 한글 2글자 이상 입력하세요')
        return
      }
      this.grade = null
      this.room = null
      this.$emit('search-by-name', this.date, this.name)
    },
  },
}
</script>

<style scoped>
.hidden {
  visibility: hidden;
}
</style>
