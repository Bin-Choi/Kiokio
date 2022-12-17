<template>
  <div style="margin-bottom: 1vh">
    <div
      class="d-flex justify-content-between"
      style="margin: 0 0 2vh 0; font-size: 3vh"
    >
      <font-awesome-icon
        icon="fa-solid fa-circle-arrow-left"
        @click="$router.push({ name: 'admin' })"
        style="cursor: pointer"
      />
      <div>출결 관리</div>
      <div></div>
    </div>

    <div class="d-flex justify-content-start" style="margin-bottom: 1vh">
      <span> ※ 필수 입력값입니다.</span>
    </div>

    <div class="d-flex justify-content-between">
      <div>
        <input
          type="number"
          min="2000"
          class="student-search-form"
          ref="year"
          v-model.trim="year"
        />
        <span>년</span>
        <input
          type="number"
          min="1"
          max="12"
          class="student-search-form"
          ref="month"
          v-model.trim="month"
        />
        <span>월</span>
      </div>

      <div class="d-flex">
        <div style="margin-right: 2vh">
          <span>학년</span>
          <input
            type="number"
            min="1"
            class="student-search-form"
            ref="grade"
            v-model.trim="grade"
            @keyup.enter="$refs.room.focus()"
          />
          <span>반</span>
          <input
            type="number"
            min="1"
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
  </div>
</template>

<script>
export default {
  name: 'StudentHeader',
  data() {
    return {
      year: null,
      month: null,
      grade: null,
      room: null,
      name: null,
    }
  },
  methods: {
    searchByClass() {
      if (!this.year || !this.month) {
        alert('년, 월을 모두 입력해주세요')
      }
      // 년 검사
      const regYear = /^\d{4}$/
      if (!regYear.test(this.year)) {
        alert('년도를 4개의 숫자로 입력해주세요')
        return
      }
      // 월 검사
      const regMonth = /^[1-9]$|^1[012]$/
      if (!regMonth.test(this.month)) {
        alert('월은 1~12의 숫자로 입력해주세요')
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
      this.$emit(
        'search-by-class',
        this.year,
        this.month,
        this.grade,
        this.room
      )
    },
    searchByName() {
      if (!this.year || !this.month) {
        alert('년, 월을 입력하세요')
      }
      // 년 검사
      const regYear = /^\d{4}$/
      if (!regYear.test(this.year)) {
        alert('년도를 4개의 숫자로 입력해주세요')
        return
      }
      // 월 검사
      const regMonth = /^[1-9]$|^1[012]$/
      if (!regMonth.test(this.month)) {
        alert('월은 1~12의 숫자로 입력해주세요')
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
      this.$emit('search-by-name', this.year, this.month, this.name)
    },
  },
}
</script>

<style></style>
