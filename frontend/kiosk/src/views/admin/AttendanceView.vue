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
      <AttendHeader
        @search-by-class="searchByClass"
        @search-by-name="searchByName"
        @download-excel="downloadExcel"
        :students="students"
      />
      <div id="admin-scroll-box" style="overflow-x: scroll; overflow-y: scroll">
        <table v-if="students" id="attendance-table">
          <AttendanceTableColumn :days="days" />
          <AttendanceItem
            v-for="student in students"
            :key="student.id"
            :student="student"
            :days="days"
          />
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import AdminHeader from '@/components/admin/common/AdminHeader.vue'
import AttendHeader from '@/components/admin/attend/AttendHeader.vue'
import AttendanceTableColumn from '@/components/admin/attend/AttendanceTableColumn.vue'
import AttendanceItem from '@/components/admin/attend/AttendanceItem.vue'

import axiosAuth from '@/axios/axios'
import * as XLSX from 'xlsx'

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
  name: 'AttendanceView',
  components: {
    AdminHeader,
    AttendHeader,
    AttendanceTableColumn,
    AttendanceItem,
  },
  data() {
    return {
      year: 22,
      month: 12,
      students: null,
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
    // Read
    searchByClass(year, month, grade, room) {
      this.year = year
      this.month = month
      this.grade = grade
      this.room = room
      this.name = null
      const url = `${this.axios_URL}/students/${year}/${month}/${grade}/${room}/attendance/`
      this.searchStudent(url)
    },
    searchByName(year, month, name) {
      this.year = year
      this.month = month
      this.grade = null
      this.room = null
      this.name = name
      const url = `${this.axios_URL}/students/${year}/${month}/${name}/attendance/`
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
          // console.log(res)
          this.students = res.data
        })
        .catch(() => {
          // console.error(err)
          alert('해당 정보의 학생이 존재하지 않습니다')
        })
    },
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
