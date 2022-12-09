<template>
  <div
    class="bg-white d-flex flex-column align-items-center"
    style="width: 100vw; height: 100vh; padding: 7vh">
    <AdminHeader />
    <div
      class="bg-secondary rounded shadow d-flex flex-column"
      style="width: 100%; height: 80vh; padding: 3vh; margin-top: 5vh">
      <StudentHeader
        @search-by-class="searchByClass"
        @search-by-name="searchByName" />
      <div v-if="students">
        <div v-if="mode === 'R'">
          <button class="blue-btn" @click="mode = 'U'">수정</button>
          <button class="red-btn" @click="mode = 'D'">삭제</button>
        </div>
        <div v-if="mode === 'U'">
          <button class="blue-btn" @click="updateStudent">저장</button>
        </div>
        <div v-if="mode === 'D'">
          <button class="red-btn" @click="deleteStudent">삭제</button>
        </div>
      </div>
      <div style="overflow-y: scroll">
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
import axios from 'axios'

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
      axios({
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
      }
      axios({
        method: 'put',
        url: `${this.axios_URL}/students/`,
        headers: {
          Authorization: `Bearer ${this.access}`,
        },
        data: this.students,
      })
        .then((res) => {
          console.log(res)
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

      axios({
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

<style>
.green-btn {
  background-color: rgb(109, 163, 28);
  width: 10vw;
  height: 5vh;
  border-radius: 1vh;

  border: 0;
  outline: 0;

  color: white;
  font-size: 2vh;
  font-weight: bold;
}
.green-btn:focus {
  outline: 2px solid black;
}
.green-btn:hover {
  background-color: rgb(13, 81, 17);
}
.red-btn {
  background-color: rgb(193, 32, 42);
  width: 10vw;
  height: 5vh;
  border-radius: 1vh;

  border: 0;
  outline: 0;

  color: white;
  font-size: 2vh;
  background-color: #2b64aa1e;
  width: 11vh;
  padding: 0.5vh;
  margin: 0 1vh;
}
.red-btn:focus {
  outline: 2px solid black;
}
.red-btn:hover {
  background-color: rgb(123, 18, 18);
}
.blue-btn {
  background-color: rgb(30, 30, 148);
  width: 10vw;
  height: 5vh;
  border-radius: 1vh;

  border: 0;
  outline: 0;

  color: white;
  font-size: 2vh;
  font-weight: bold;
}
.blue-btn:focus {
  outline: 2px solid black;
}
.blue-btn:hover {
  background-color: rgb(18, 28, 115);
}
</style>
