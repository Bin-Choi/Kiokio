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

import * as XLSX from 'xlsx'

export default {
  name: 'StudentView',
  components: {
    AdminHeader,
    StudentHeader,
  },
  methods: {
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

<style></style>
