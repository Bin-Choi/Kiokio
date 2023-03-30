<template>
  <div>
    <div class="d-flex justify-content-between">
      <TheButton
        :text="'취소'"
        :onClick="() => $router.push({ name: 'student', query })"
      />
      <TheButton :text="'확인'" :onClick="updateStudent" />
    </div>

    <StudentLabel />
    <div id="admin-scroll-box">
      <StudentUpdateItem
        v-for="(student, index) in students"
        :key="student.id"
        :index="index"
        :student="student"
        :invalid="invalid"
        @change-data="changeData"
      />
    </div>
  </div>
</template>

<script>
import TheButton from '../common/TheButton.vue'
import StudentLabel from './StudentLabel.vue'
import StudentUpdateItem from './StudentUpdateItem.vue'

import axiosAuth from '@/axios/axios'

export default {
  name: 'StudentUpdate',
  components: {
    StudentLabel,
    StudentUpdateItem,
    TheButton,
  },
  data() {
    return {
      invalid: null,
      selected: [],
      grade: null,
      room: null,
      name: null,
    }
  },
  computed: {
    axios_URL() {
      return this.$store.state.axios_URL
    },
    access() {
      return this.$store.state.access
    },
    students() {
      return this.$store.state.students
    },
    query() {
      return this.$store.state.query
    },
  },
  methods: {
    changeData(value, index, key) {
      this.students[index][key] = value
    },
    updateStudent() {
      // 중복 검사를 통과한 학생 리스트
      let studentsList = []

      //유효성 검사
      this.invalid = null
      const students = this.students
      for (let i = 0; i < students.length; i++) {
        //이름검사
        const regName = /^[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]{2,}$/
        if (!regName.test(students[i].name)) {
          this.invalid = i
          alert('이름은 한글 2글자 이상 입력하세요')
          return
        }
        //학년 검사
        const regGrade = /^[1-9]$/
        if (!regGrade.test(students[i].grade)) {
          this.invalid = i
          alert('학년은 1~9사이의 숫자로 입력하세요')
          return
        }
        //반 검사
        const regRoom = /^[1-9]$|^[1-9]{1}[0-9]{1}$/
        if (!regRoom.test(students[i].room)) {
          this.invalid = i
          alert('반은 1~99사이의 숫자로 입력하세요')
          return
        }
        //번호 검사
        const regNumber = /^[1-9]$|^[1-9]{1}[0-9]{1}$/
        if (!regNumber.test(students[i].number)) {
          this.invalid = i
          alert('번호는 1~99사이의 숫자로 입력하세요')
          return
        }
        //성별 검사
        if (!(students[i].gender === '남성' || students[i].gender === '여성')) {
          this.invalid = i
          alert('성별을 선택하세요')
          return
        }
        //비밀번호 검사
        const regPassword = /^[0-9]{4}$/
        if (!regPassword.test(students[i].password)) {
          this.invalid = i
          alert('비밀번호는 4자리 숫자로 입력하세요')
          return
        }
        // 학번 중복인 학생 필터링
        if (studentsList) {
          for (let j = 0; j < studentsList.length; j++) {
            if (
              studentsList[j].grade === students[i].grade &&
              studentsList[j].room === students[i].room &&
              studentsList[j].number === students[i].number
            ) {
              alert(
                `${students[i].grade}학년 ${students[i].room}반 ${students[i].number}번 학생이 중복으로 존재합니다.`
              )
              return
            }
          }
        }
      }
      axiosAuth({
        method: 'put',
        url: `${this.axios_URL}/students/`,
        headers: {
          Authorization: `Bearer ${this.access}`,
        },
        data: this.students,
      })
        .then(() => {
          let url
          if (this.$route.query.name)
            url = `students/${this.$route.query.name}/`
          else
            url = `students/${this.$route.query.grade}/${this.$route.query.room}/`

          this.$store.dispatch('getStudents', url)
          this.$router.push({ name: 'student', query: this.$route.query })
        })
        .catch((err) => {
          console.error(err)
          alert('새로고침 후 다시 시도해주세요')
        })
    },
  },
}
</script>

<style scoped>
button {
  margin-bottom: 0.5vh;
}
</style>
