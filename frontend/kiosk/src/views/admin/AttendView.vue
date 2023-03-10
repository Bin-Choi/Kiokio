<template>
  <div
    class="bg-white d-flex flex-column"
    style="width: 100vw; height: 100vh; padding: 7vh"
  >
    <AdminHeader />

    <div
      class="rounded shadow d-flex flex-column"
      style="
        width: 100%;
        height: 80vh;
        padding: 3vh;
        margin-top: 3vh;
        background-color: #81a0bb4b;
        min-width: 750px;
      "
    >
      <AttendHeader @download-excel="downloadExcel" />

      <router-view />
    </div>
  </div>
</template>

<script>
import AdminHeader from '@/components/admin/common/AdminHeader.vue'
import AttendHeader from '@/components/admin/attend/AttendHeader.vue'

import * as XLSX from 'xlsx'

export default {
  name: 'AttendView',
  components: {
    AdminHeader,
    AttendHeader,
  },
  data() {
    return {
      year: 22,
      month: 12,
      grade: null,
      room: null,
      name: null,
    }
  },

  methods: {
    downloadExcel() {
      let fileName = ''
      if (this.name) {
        fileName = `${this.year}년_${this.month}월_${this.name}_키오스크_출석현황.xlsx`
      } else {
        fileName = `${this.year}년_${this.month}월_${this.grade}학년_${this.room}반_키오스크_출석현황.xlsx`
      }
      const excelData = XLSX.utils.table_to_sheet(
        document.getElementById('attendance-table')
      ) // table id를 넣어주면된다
      const workBook = XLSX.utils.book_new() // 새 시트 생성
      XLSX.utils.book_append_sheet(workBook, excelData, '출석현황') // 시트 명명, 데이터 지정
      XLSX.writeFile(workBook, fileName) // 엑셀파일 만듬
    },
  },
}
</script>

<style></style>
