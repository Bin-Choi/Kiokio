<template>
  <div>
    <div class="d-flex justify-content-between">
      <div class="d-flex">
        <TheInput
          :label="'년'"
          :type="'number'"
          :min="2000"
          :refer="'year'"
          :value="year"
          :display="'right'"
          @change="
            (v) => {
              this.year = v
            }
          "
        />
        <TheInput
          :label="'월'"
          :type="'number'"
          :min="1"
          :max="12"
          :refer="'month'"
          :value="month"
          :display="'right'"
          @change="
            (v) => {
              this.month = v
            }
          "
        />
      </div>

      <div class="d-flex">
        <!-- <span>학년</span>
          <input
            type="number"
            min="1"
            class="student-search-form"
            ref="grade"
            v-model.trim="grade"
            @keyup.enter="$refs.room.focus()"
          /> -->

        <TheInput
          :label="'학년'"
          :type="'number'"
          :min="1"
          :refer="'grade'"
          :value="grade"
          :display="'right'"
          @change="
            (v) => {
              this.grade = v
            }
          "
        />
        <TheInput
          :label="'반'"
          :type="'number'"
          :min="1"
          :refer="'room'"
          :value="room"
          :submit="searchByClass"
          :display="'right'"
          @change="
            (v) => {
              this.room = v
            }
          "
        />
        <TheButton :text="'학급 조회'" :onClick="searchByClass" />

        <TheInput
          :label="'이름'"
          :refer="'name'"
          :value="name"
          :submit="searchByName"
          @change="
            (v) => {
              this.name = v
            }
          "
        />
        <TheButton :text="'이름 조회'" :onClick="searchByName" />
      </div>
    </div>

    <div id="admin-scroll-box" style="overflow: scroll">
      <table v-if="students?.length" id="attendance-table">
        <AttendLabel :days="days" />
        <AttendReadItem
          v-for="student in students"
          :key="student.id"
          :student="student"
          :days="days"
        />
      </table>
    </div>
  </div>
</template>

<script>
import AttendReadItem from '@/components/admin/attend/AttendReadItem.vue'
import AttendLabel from '@/components/admin/attend/AttendLabel.vue'
import TheButton from '@/components/admin/common/TheButton.vue'
import TheInput from '@/components/admin/common/TheInput.vue'

const daysOfMonth = {
  1: 31,
  2: 28,
  3: 31,
  4: 30,
  5: 31,
  6: 30,
  7: 31,
  8: 31,
  9: 30,
  10: 31,
  11: 30,
  12: 31,
}

export default {
  name: 'AttendRead',
  components: {
    AttendLabel,
    AttendReadItem,
    TheButton,
    TheInput,
  },
  data() {
    return {
      year: null,
      month: null,
      grade: null,
      room: null,
      name: null,
    }
  },
  computed: {
    students() {
      return this.$store.state.students
    },
    days() {
      const year = parseInt(this.year)
      const month = parseInt(this.month)
      if (
        month == 2 &&
        (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0))
      ) {
        return 29
      } else {
        return daysOfMonth[`${month}`]
      }
    },
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

      const url = `/students/${this.year}/${this.month}/${this.grade}/${this.room}/attendance/`
      this.$store.dispatch('getStudents', url)

      this.name = null
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

      // 이름 검사
      const regName = /^[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]{2,}$/
      if (!regName.test(this.name)) {
        alert('이름은 한글 2글자 이상 입력하세요')
        return
      }

      const url = `/students/${this.year}/${this.month}/${this.name}/attendance/`
      this.$store.dispatch('getStudents', url)

      this.grade = null
      this.room = null
    },
  },
}
</script>

<style></style>
