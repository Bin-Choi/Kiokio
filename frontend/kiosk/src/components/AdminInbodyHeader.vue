<template>
  <div class="d-flex flex-column" style="margin-bottom: 1vh; min-width: 710px">
    <div
      class="d-flex justify-content-between"
      style="margin: 0 0 2vh 0; font-size: 3vh"
    >
      <font-awesome-icon
        icon="fa-solid fa-circle-arrow-left"
        @click="
          $router.push({ name: 'admin' })
          $store.state.inbodyStudents = null
        "
        style="cursor: pointer"
      />
      <div>인바디 관리</div>
      <div></div>
    </div>
    <div style="text-align: left; padding-left: 0.3vh">* 선택 값입니다.</div>
    <div class="d-flex justify-content-between">
      <div>
        <input
          type="date"
          class="student-search-form"
          style="width: 13vh"
          ref="startDate"
          v-model="startDate"
        />
        ~
        <input
          type="date"
          class="student-search-form"
          style="width: 13vh"
          ref="endDate"
          v-model="endDate"
        />
      </div>
      <div>
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
          @keyup.enter="searchByClass"
        />
        <button class="blue-btn shadow-sm" @click="searchByClass">
          학급 조회
        </button>
        <span style="margin-left: 3vh">이름</span>
        <input
          type="text"
          class="student-search-form"
          ref="name"
          v-model.trim="name"
          @keyup.enter="searchByName"
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
  name: "AdminInbodyHeader",
  data() {
    return {
      startDate: null,
      endDate: null,
      grade: null,
      room: null,
      name: null,
    }
  },
  methods: {
    searchByClass() {
      if (!this.grade || !this.room) {
        alert("학년, 반을 모두 입력해주세요")
        return
      }
      //학년 검사
      const regGrade = /^[1-9]$/
      if (!regGrade.test(this.grade)) {
        alert("학년은 1~9사이의 숫자로 입력하세요")
        return
      }
      //반 검사
      const regRoom = /^[1-9]$|^[1-9]{1}[0-9]{1}$/
      if (!regRoom.test(this.room)) {
        alert("반은 1~99사이의 숫자로 입력하세요")
        return
      }
      this.name = null
      this.$emit(
        "search-by-class",
        this.startDate,
        this.endDate,
        this.grade,
        this.room
      )
    },
    searchByName() {
      if (!this.name) {
        alert("이름을 입력해주세요")
        return
      }
      const regName = /^[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]{2,}$/
      if (!regName.test(this.name)) {
        alert("이름은 한글 2글자 이상 입력하세요")
        return
      }
      this.grade = null
      this.room = null
      this.$emit("search-by-name", this.startDate, this.endDate, this.name)
    },
  },
}
</script>

<style></style>
