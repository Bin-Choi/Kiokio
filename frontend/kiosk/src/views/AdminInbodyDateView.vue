<template>
  <div
    class="bg-white d-flex flex-column align-items-center"
    style="height: 100vh; padding: 7vh">
    <AdminHeader />

    <div class="inbodyContent rounded shadow d-flex flex-column">
      <AdminInbodyDateHeader
        @search-by-class="searchByClass"
        @search-by-name="searchByName"
        @download-excel="downloadExcel"
        :inbody-students="inbodyStudents"
        :mode="mode" />

      <div v-if="inbodyStudents">
        <!-- INBODY CONTENT -->
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

        <div
          id="admin-scroll-box"
          style="height: 60vh; overflow-x: scroll; overflow-y: scroll">
          <div v-if="mode === 'R'">
            <table style="margin-bottom: 0.5vh" id="inbody-date-table">
              <AdminInbodyDateTableColumn />
              <AdminInbodyDateReadItem
                v-for="(inbody, index) in inbodyStudents"
                :key="inbody.id"
                :inbody="inbody"
                :index="index" />
            </table>
          </div>
          <div v-if="mode === 'U'">
            <table style="margin-bottom: 0.5vh">
              <AdminInbodyDateTableColumn />
              <AdminInbodyDateUpdateItem
                v-for="(student, index) in inbodyStudents"
                :key="student.id"
                :student="student"
                :index="index" />
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AdminHeader from '@/components/AdminHeader.vue'
import AdminInbodyDateHeader from '@/components/AdminInbodyDateHeader.vue'
import AdminInbodyDateTableColumn from '@/components/AdminInbodyDateTableColumn.vue'
import AdminInbodyDateReadItem from '@/components/AdminInbodyDateReadItem.vue'
import AdminInbodyDateUpdateItem from '@/components/AdminInbodyDateUpdateItem.vue'
import axiosAuth from '@/axios/axios'
import * as XLSX from 'xlsx'

export default {
  name: 'AdminInbodyDateView',
  components: {
    AdminHeader,
    AdminInbodyDateHeader,
    AdminInbodyDateTableColumn,
    AdminInbodyDateReadItem,
    AdminInbodyDateUpdateItem,
  },
  data() {
    return {
      mode: 'R',
      date: null,
      name: null,
      grade: null,
      room: null,
    }
  },
  computed: {
    axios_URL() {
      return this.$store.state.axios_URL
    },
    access() {
      return this.$store.state.access
    },
    inbodyStudents() {
      return this.$store.state.inbodyStudents
    },
  },
  methods: {
    // Read
    searchByClass(date, grade, room) {
      this.date = date
      this.grade = grade
      this.room = room
      this.name = null
      const url = `${this.axios_URL}/students/${date}/${grade}/${room}/inbody/admin/date/`
      this.searchStudent(url)
    },
    searchByName(date, name) {
      this.date = date
      this.grade = null
      this.room = null
      this.name = name
      const url = `${this.axios_URL}/students/${date}/${name}/inbody/admin/date/`
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
          this.$store.commit('SAVE_INBODY_STUDENTS', res.data)
        })
        .catch((err) => {
          console.error(err)
          alert('해당 정보의 학생이 존재하지 않습니다')
        })
    },
    downloadExcel() {
      let fileName = ''
      if (this.name) {
        fileName = `${this.date}_${this.name}_인바디기록.xlsx`
      } else {
        fileName = `${this.date}_${this.grade}학년_${this.room}반_인바디기록.xlsx`
      }
      const excelData = XLSX.utils.table_to_sheet(
        document.getElementById('inbody-date-table')
      ) // table id를 넣어주면된다
      const workBook = XLSX.utils.book_new() // 새 시트 생성
      XLSX.utils.book_append_sheet(workBook, excelData, '인바디기록') // 시트 명명, 데이터 지정
      XLSX.writeFile(workBook, fileName) // 엑셀파일 만듬
    },
  },
}
</script>

<style scoped>
.inbodyContent {
  width: 100%;
  height: 80vh;
  padding: 3vh;
  margin-top: 3vh;
  background-color: #81a0bb4b;
  min-width: 750px;
}
</style>
