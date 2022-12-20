<template>
  <div>
    <div class="d-flex justify-content-between">
      <div></div>

      <div class="d-flex">
        <font-awesome-icon
          icon="fa-regular fa-file-powerpoint"
          @click="print"
          style="font-size: 3.6vh" />
        <button
          class="blue-btn shadow-sm"
          @click="$emit('change-mode-U')"
          style="margin-left: 1vh">
          수정
        </button>
        <button
          class="red-btn shadow-sm"
          style="margin-left: 1vh"
          @click="deleteInbody">
          삭제
        </button>
      </div>
    </div>

    <!-- INBODY CONTENT -->
    <div id="printContent" style="font-size: 2.3vh; padding: 2vh">
      <div class="w-100" style="font-size: 2.5vh; margin-bottom: 5vh">
        {{ student.grade }}학년 {{ student.room }}반 {{ student.number }}번
        {{ student.name }} ({{ student.gender }})
      </div>
      <div
        id="admin-scroll-box"
        class="w-75 d-flex m-auto justify-content-evenly">
        <table class="container">
          <tr class="row">
            <td class="col-6">검사일시</td>
            <td class="col-4 rounded shadow-sm">{{ inbody.test_date }}</td>
          </tr>

          <tr class="row">
            <td class="col-6">키</td>
            <td class="col-4 rounded shadow-sm">{{ inbody.height }}</td>
            <td class="col-1">cm</td>
          </tr>

          <tr class="row">
            <td class="col-6">나이</td>
            <td class="col-4 rounded shadow-sm">{{ inbody.age }}</td>
            <td class="col-1">세</td>
          </tr>

          <tr class="row">
            <td class="col-6">체중</td>
            <td class="col-4 rounded shadow-sm">{{ inbody.weight }}</td>
            <td class="col-1">kg</td>
          </tr>

          <tr class="row">
            <td class="col-6">BMI</td>
            <td class="col-4 rounded shadow-sm">
              {{ inbody.body_mass_index }}
            </td>
            <td class="col-1">kg/m<sup>2</sup></td>
          </tr>

          <tr class="row">
            <td class="col-6">체지방률</td>
            <td class="col-4 rounded shadow-sm">
              {{ inbody.percent_body_fat }}
            </td>
            <td class="col-1">%</td>
          </tr>
        </table>

        <table class="container">
          <tr class="row">
            <td class="col-6">체수분</td>
            <td class="col-4 rounded shadow-sm">
              {{ inbody.total_body_water }}
            </td>
            <td class="col-1">L</td>
          </tr>

          <tr class="row">
            <td class="col-6">단백질</td>
            <td class="col-4 rounded shadow-sm">{{ inbody.protein }}</td>
            <td class="col-1">kg</td>
          </tr>

          <tr class="row">
            <td class="col-6">무기질</td>
            <td class="col-4 rounded shadow-sm">{{ inbody.minerals }}</td>
            <td class="col-1">kg</td>
          </tr>

          <tr class="row">
            <td class="col-6">체지방량</td>
            <td class="col-4 rounded shadow-sm">
              {{ inbody.body_fat_mass }}
            </td>
            <td class="col-1">kg</td>
          </tr>

          <tr class="row">
            <td class="col-6">골격근량</td>
            <td class="col-4 rounded shadow-sm">
              {{ inbody.skeletal_muscle_mass }}
            </td>
            <td class="col-1">kg</td>
          </tr>

          <tr class="row">
            <td class="col-6">인바디 점수</td>
            <td class="col-4 rounded shadow-sm">
              {{ inbody.inbody_score }}
            </td>
            <td class="col-1">점</td>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axiosAuth from '@/axios/axios'
import printJS from 'print-js'

export default {
  name: 'AdminInbodyDetailRead',
  props: {
    studentIndex: Number,
    inbodyIndex: Number,
  },
  computed: {
    axios_URL() {
      return this.$store.state.axios_URL
    },
    access() {
      return this.$store.state.access
    },
    student() {
      return this.$store.state.inbodyStudents[this.studentIndex]
    },
    inbody() {
      return this.$store.state.inbodyStudents[this.studentIndex].inbody_set[
        this.inbodyIndex
      ]
    },
  },
  methods: {
    deleteInbody() {
      axiosAuth({
        method: 'delete',
        url: `${this.axios_URL}/students/inbody/${this.inbody.id}/admin/`,
        headers: {
          Authorization: `Bearer ${this.access}`,
        },
      })
        .then((res) => {
          console.log(res)
          const payload = {
            studentIndex: this.studentIndex,
            inbodyIndex: this.inbodyIndex,
          }
          this.$store.commit('DELETE_STUDENT_INBODY_DETAIL', payload)
          this.$emit('change-mode-default')
        })
        .catch((err) => {
          console.error(err)
        })
    },
    print() {
      printJS({
        printable: 'printContent',
        type: 'html',
        scanStyles: false,
      })
    },
  },
}
</script>

<style scoped>
.row {
  margin: 2.5vh 0;
  align-items: baseline;
}

.col-4 {
  background-color: white;
  border: 0.3vh solid rgba(129, 160, 187, 0.452);
  padding: 0.5vh 0;
  min-width: 52px;
}
</style>
