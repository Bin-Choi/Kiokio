<template>
  <div
    class="bg-white d-flex flex-column align-items-center"
    style="width: 100vw; height: 100vh; padding: 7vh"
  >
    <AdminHeader />
    <div
      id="content"
      class="w-100 rounded shadow-sm d-flex flex-column content"
      style="
        height: 80vh;
        padding: 3vh;
        margin-top: 3vh;
        background-color: #81a0bb4b;
      "
    >
      <StudentHeader @download-excel="downloadExcel" />

      <router-view />
    </div>
  </div>
</template>

<script>
import AdminHeader from '@/components/admin/common/AdminHeader.vue'
import StudentHeader from '@/components/admin/student/StudentHeader.vue'

import axiosAuth from '@/axios/axios'
import * as XLSX from 'xlsx'

export default {
  name: 'StudentView',
  components: {
    AdminHeader,
    StudentHeader,
  },
  data() {
    return {
      students: null,
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
      this.grade = grade
      this.room = room
      this.name = null
      const url = `${this.axios_URL}/students/${grade}/${room}/`
      this.searchStudent(url)
    },
    searchByName(name) {
      this.grade = null
      this.room = null
      this.name = name
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
          console.log(this.students)
          this.mode = 'R'
        })
        .catch((err) => {
          console.error(err)
          alert('해당 정보의 학생이 존재하지 않습니다')
        })
    },
    downloadExcel() {
      let fileName = ''
      if (this.name) {
        fileName = `${this.name}_키오스크_학생정보.xlsx`
      } else {
        fileName = `${this.grade}학년_${this.room}반_키오스크_학생정보.xlsx`
      }
      const excelData = XLSX.utils.table_to_sheet(
        document.getElementById('student-table')
      ) // table id를 넣어주면된다
      const workBook = XLSX.utils.book_new() // 새 시트 생성
      XLSX.utils.book_append_sheet(workBook, excelData, '학생정보') // 시트 명명, 데이터 지정
      XLSX.writeFile(workBook, fileName) // 엑셀파일 만듬
    },
  },
}
</script>

<style scoped>
.button-box {
  margin-bottom: 1vh;
  display: flex;
  justify-content: end;
}
</style>
