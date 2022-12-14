<template>
  <div
    class="bg-white d-flex flex-column align-items-center"
    style="width: 100vw; height: 100vh; padding: 7vh">
    <AdminHeader />
    <div
      id="content"
      class="w-100 rounded shadow-sm d-flex flex-column content"
      style="
        height: 80vh;
        padding: 3vh;
        margin-top: 5vh;
        background-color: #81a0bb4b;
      ">
      <StudentHeader
        @search-by-class="searchByClass"
        @search-by-name="searchByName" />

      <div v-if="students">
        <div id="button-box" v-if="mode === 'R'">
          <button class="blue-btn shadow-sm" @click="mode = 'U'">수정</button>
          <button
            class="red-btn shadow-sm"
            style="margin-left: 1vh"
            @click="mode = 'D'">
            삭제
          </button>
        </div>

        <div id="button-box" v-if="mode === 'U'">
          <button class="blue-btn shadow-sm" @click="updateStudent">
            저장
          </button>
        </div>

        <div id="button-box" v-if="mode === 'D'">
          <button class="red-btn shadow-sm" @click="deleteStudent">삭제</button>
        </div>
      </div>
      <div id="admin-scroll-box" style="overflow-y: scroll">
        <StudentTableColumn />
        <div v-if="students && mode === 'R'">
          <StudentReadItem
            v-for="(student, index) in students"
            :key="student.id"
            :index="index"
            :student="student" />
        </div>
        <div v-if="students && mode === 'U'">
          <StudentUpdateItem
            v-for="(student, index) in students"
            :key="index"
            :index="index"
            :student="student"
            :invalid="invalid"
            @change-data="changeData" />
        </div>
        <div v-if="students && mode === 'D'">
          <StudentDeleteItem
            v-for="(student, index) in students"
            :key="index"
            :index="index"
            :student="student"
            @change-check="changeCheck" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AdminHeader from '@/components/AdminHeader.vue'
import StudentTableColumn from '@/components/StudentTableColumn.vue'
import StudentHeader from '@/components/StudentHeader.vue'
import StudentReadItem from '@/components/StudentReadItem.vue'
import StudentUpdateItem from '@/components/StudentUpdateItem.vue'
import StudentDeleteItem from '@/components/StudentDeleteItem.vue'
import axiosAuth from '@/axios/axios'

export default {
  name: 'StudentView',
  components: {
    AdminHeader,
    StudentTableColumn,
    StudentHeader,
    StudentReadItem,
    StudentUpdateItem,
    StudentDeleteItem,
  },
  data() {
    return {
      students: null,
      mode: 'R',
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
    // Read
    searchByClass(grade, room) {
      const url = `${this.axios_URL}/students/${grade}/${room}/`
      this.searchStudent(url)
    },
    searchByName(name) {
      const url = `${this.axios_URL}/students/${name}/`
      this.searchStudent(url)
    },
    searchStudent(url) {
      axiosAuth({
        method: 'get',
        url: url,
        headers: {
          Authorization: `Bearer ${this.access}`,
        },
      })
        .then((res) => {
          console.log(res)
          this.students = res.data
          this.mode = 'R'
        })
        .catch((err) => {
          console.error(err)
          alert('해당 정보의 학생이 존재하지 않습니다')
        })
    },
    // Update
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
          this.mode = 'R'
        })
        .catch((err) => {
          console.error(err)
        })
    },
    // Delete
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
    deleteStudent() {
      let delete_list = []
      for (const index of this.selected) {
        delete_list.push(this.students[index].id)
      }
      axiosAuth({
        method: 'delete',
        url: `${this.axios_URL}/students/`,
        headers: {
          Authorization: `Bearer ${this.access}`,
        },
        data: delete_list,
      })
        .then((res) => {
          console.log(res)
          this.selected.sort(function compare(a, b) {
            return b - a
          })
          this.selected.forEach((index) => {
            this.students.splice(index, 1)
          })
          this.selected = []
          this.mode = 'R'
        })
        .catch((err) => {
          console.error(err)
        })
    },
  },
}
</script>

<style scoped>
#button-box {
  margin-bottom: 1vh;
  display: flex;
  justify-content: end;
}
</style>
