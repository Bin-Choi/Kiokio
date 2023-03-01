<template>
  <div>
    <div class="content rounded shadow d-flex flex-column">
      <StudentCreateHeader
        :ready-delete="readyDelete"
        @add-row="addRow"
        @delete-row="deleteRow"
        @create-student="createStudent"
      />
      <div id="admin-scroll-box">
        <table style="min-width: 360px">
          <StudentTableColumn />
          <StudentCreateItem
            v-for="(student, index) in students"
            :key="index"
            :index="index"
            :student="student"
            :ready-delete="readyDelete"
            :invalid="invalid"
            @change-check="changeCheck"
            @change-data="changeData"
          />
        </table>
      </div>
    </div>
  </div>
</template>

<script>
// import AdminHeader from '@/components/admin/common/AdminHeader.vue'
import StudentCreateHeader from '@/components/admin/student/StudentCreateHeader.vue'
import StudentTableColumn from '@/components/admin/student/StudentTableColumn.vue'
import StudentCreateItem from '@/components/admin/student/StudentCreateItem.vue'

import axiosAuth from '@/axios/axios'

export default {
  name: 'StudentCreateView',
  components: {
    // AdminHeader,
    StudentCreateHeader,
    StudentTableColumn,
    StudentCreateItem,
  },
  data() {
    return {
      students: [
        {
          name: null,
          grade: null,
          room: null,
          number: null,
          gender: null,
          password: '0000',
        },
      ],
      readyDelete: false,
      invalid: null,
      selected: [],
    }
  },
  computed: {
    axios_URL() {
      return this.$store.state.axios_URL
    },
    access() {
      return this.$store.state.access
    },
  },
  methods: {
    // Create Row
    addRow() {
      this.students.push({
        name: null,
        grade: null,
        room: null,
        number: null,
        gender: null,
        password: '0000',
      })
    },
    // Delete Rows
    changeCheck(value, index) {
      if (value) {
        this.selected.push(index)
      } else {
        for (let i = 0; i < this.selected.length; i++) {
          if (this.selected[i] === index) {
            this.selected.splice(i, 1)
            break
          }
        }
      }
    },
    deleteRow() {
      if (!this.readyDelete) {
        this.readyDelete = true
      } else {
        this.selected.sort(function compare(a, b) {
          return b - a
        })
        this.selected.forEach((index) => {
          this.students.splice(index, 1)
        })
        this.selected = []
        this.readyDelete = false
      }
    },
    // Insert & Create
    changeData(value, index, key) {
      this.students[index][key] = value.trim()
    },
    createStudent() {
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
        studentsList.push(students[i])
      }
      axiosAuth({
        method: 'post',
        url: `${this.axios_URL}/students/`,
        headers: {
          Authorization: `Bearer ${this.access}`,
        },
        data: this.students,
      })
        .then(() => {
          alert('성공적으로 저장됐습니다.')
          this.students = [
            { name: null, grade: null, room: null, number: null, gender: null },
          ]
          this.$router.push({ name: 'student' })
        })
        .catch(() => {
          alert('학번이 중복된 학생 데이터가 존재합니다.')
        })
    },
  },
}
</script>

<style scoped>
.content {
  width: 100%;
  height: 80vh;
  padding: 3vh;
  margin-top: 3vh;
  background-color: #81a0bb4b;
  min-width: 440px;
}
</style>
