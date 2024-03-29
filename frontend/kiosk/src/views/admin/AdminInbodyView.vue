<template>
  <div
    class="bg-white d-flex flex-column align-items-center"
    style="height: 100vh; padding: 7vh"
  >
    <AdminHeader />

    <div class="inbodyContent rounded shadow d-flex flex-column">
      <div v-if="mode === 'Default'">
        <InbodyHistoryHeader
          @search-by-class="searchByClass"
          @search-by-name="searchByName"
        />

        <div v-if="inbodyStudents">
          <div style="text-align: left">
            * 이름 클릭 시, 학생의 전체 기록으로 이동합니다.
          </div>
          <div style="text-align: left">
            * 인바디 기록 클릭 시, 해당 인바디의 디테일로 이동합니다.
          </div>

          <!-- INBODY CONTENT -->
          <div id="admin-scroll-box" style="height: 55vh">
            <table style="margin-bottom: 0.5vh">
              <AdminInbodyTableColumn />
              <AdminInbodyItem
                v-for="(student, index) in inbodyStudents"
                :key="student.id"
                :student="student"
                :index="index"
                @change-mode-student="changeModeStudent"
                @change-mode-detail="changeModeDetail"
              />
            </table>
          </div>
        </div>
      </div>

      <div v-if="mode === 'Student' && student">
        <InbodyStu
          :studentIndex="studentIndex"
          @change-mode-default="changeModeDefault"
        />
      </div>

      <div v-if="mode === 'Detail' && inbody">
        <AdminInbodyDetail
          :studentIndex="studentIndex"
          :inbodyIndex="inbodyIndex"
          @change-mode-default="changeModeDefault"
        />
      </div>
    </div>
  </div>
</template>

<script>
import AdminHeader from '@/components/admin/common/AdminHeader.vue'
import InbodyHistoryHeader from '@/components/admin/inbody/InbodyHistoryHeader.vue'
import AdminInbodyTableColumn from '@/components/admin/inbody/AdminInbodyTableColumn.vue'
import AdminInbodyItem from '@/components/admin/inbody/AdminInbodyItem.vue'
import InbodyStu from '@/components/admin/inbody/InbodyStu.vue'
import AdminInbodyDetail from '@/components/admin/inbody/AdminInbodyDetail.vue'

import axiosAuth from '@/axios/axios'

export default {
  name: 'AdminInbodyView',
  components: {
    AdminHeader,
    InbodyHistoryHeader,
    AdminInbodyTableColumn,
    AdminInbodyItem,
    InbodyStu,
    AdminInbodyDetail,
  },
  data() {
    return {
      mode: 'Default',
      student: null,
      inbody: null,
      studentIndex: null,
      inbodyIndex: null,
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
    searchByClass(startDate, endDate, grade, room) {
      if (!startDate) {
        startDate = '2022-01-01'
      }
      if (!endDate) {
        const date = new Date()
        const year = date.getFullYear()
        const month = ('0' + (1 + date.getMonth())).slice(-2)
        const day = ('0' + date.getDate()).slice(-2)
        endDate = year + '-' + month + '-' + day
      }
      const url = `${this.axios_URL}/students/${startDate}/${endDate}/${grade}/${room}/inbody/admin/`
      this.searchStudent(url)
    },
    searchByName(startDate, endDate, name) {
      if (!startDate) {
        startDate = '2022-01-01'
      }
      if (!endDate) {
        const date = new Date()
        const year = date.getFullYear()
        const month = ('0' + (1 + date.getMonth())).slice(-2)
        const day = ('0' + date.getDate()).slice(-2)
        endDate = year + '-' + month + '-' + day
      }
      const url = `${this.axios_URL}/students/${startDate}/${endDate}/${name}/inbody/admin/`
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
          this.$store.commit('SAVE_INBODY_STUDENTS', res.data)
        })
        .catch(() => {
          alert('해당 정보의 학생이 존재하지 않습니다')
        })
    },
    //change mode
    changeModeDefault() {
      this.mode = 'Default'
    },
    changeModeStudent(studentIndex) {
      this.mode = 'Student'
      this.studentIndex = studentIndex
      this.student = this.inbodyStudents[studentIndex]
    },
    changeModeDetail(studentIndex, inbodyIndex) {
      this.mode = 'Detail'
      this.studentIndex = studentIndex
      this.inbodyIndex = inbodyIndex
      this.student = {
        name: this.inbodyStudents[studentIndex].name,
        grade: this.inbodyStudents[studentIndex].grade,
        room: this.inbodyStudents[studentIndex].room,
        number: this.inbodyStudents[studentIndex].number,
        gender: this.inbodyStudents[studentIndex].gender,
      }
      this.inbody = this.inbodyStudents[studentIndex].inbody_set[inbodyIndex]
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
