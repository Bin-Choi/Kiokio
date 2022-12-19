<template>
  <div>
    <div class="d-flex justify-content-between">
      <div></div>

      <div class="d-flex">
        <font-awesome-icon
          icon="fa-regular fa-file-powerpoint"
          @click="print"
          style="font-size: 3.6vh"
        />
        <button
          class="blue-btn shadow-sm"
          @click="$emit('change-mode-U')"
          style="margin-left: 1vh"
        >
          수정
        </button>
        <button
          class="red-btn shadow-sm"
          style="margin-left: 1vh"
          @click="deleteInbody"
        >
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
        class="w-75 d-flex m-auto justify-content-evenly"
      >
        <div class="container">
          <div class="row">
            <span class="col-6">검사일시</span>
            <span class="col-4 rounded shadow-sm">{{ inbody.test_date }}</span>
          </div>

          <div class="row">
            <span class="col-6">키</span>
            <span class="col-4 rounded shadow-sm">{{ inbody.height }}</span>
            <span class="col-1">cm</span>
          </div>

          <div class="row">
            <span class="col-6">나이</span>
            <span class="col-4 rounded shadow-sm">{{ inbody.age }}</span>
            <span class="col-1">세</span>
          </div>

          <div class="row">
            <span class="col-6">체중</span>
            <span class="col-4 rounded shadow-sm">{{ inbody.weight }}</span>
            <span class="col-1">kg</span>
          </div>

          <div class="row">
            <span class="col-6">BMI</span>
            <span class="col-4 rounded shadow-sm">
              {{ inbody.body_mass_index }}
            </span>
            <span class="col-1">kg/m<sup>2</sup></span>
          </div>
          <div class="row">
            <span class="col-6">체지방률</span>
            <span class="col-4 rounded shadow-sm">
              {{ inbody.percent_body_fat }}
            </span>
            <span class="col-1">%</span>
          </div>
        </div>

        <div class="container">
          <div class="row">
            <span class="col-6">체수분</span>
            <span class="col-4 rounded shadow-sm">
              {{ inbody.total_body_water }}
            </span>
            <span class="col-1">L</span>
          </div>

          <div class="row">
            <span class="col-6">단백질</span>
            <span class="col-4 rounded shadow-sm">{{ inbody.protein }}</span>
            <span class="col-1">kg</span>
          </div>

          <div class="row">
            <span class="col-6">무기질</span>
            <span class="col-4 rounded shadow-sm">{{ inbody.minerals }}</span>
            <span class="col-1">kg</span>
          </div>

          <div class="row">
            <span class="col-6">체지방량</span>
            <span class="col-4 rounded shadow-sm">
              {{ inbody.body_fat_mass }}
            </span>
            <span class="col-1">kg</span>
          </div>

          <div class="row">
            <span class="col-6">골격근량</span>
            <span class="col-4 rounded shadow-sm">
              {{ inbody.skeletal_muscle_mass }}
            </span>
            <span class="col-1">kg</span>
          </div>

          <div class="row">
            <span class="col-6">인바디 점수</span>
            <span class="col-4 rounded shadow-sm">
              {{ inbody.inbody_score }}
            </span>
            <span class="col-1">점</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axiosAuth from "@/axios/axios"
import printJS from "print-js"

export default {
  name: "AdminInbodyDetailRead",
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
        method: "delete",
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
          this.$store.commit("DELETE_STUDENT_INBODY_DETAIL", payload)
          this.$emit("change-mode-default")
        })
        .catch((err) => {
          console.error(err)
        })
    },
    print() {
      printJS({
        printable: "printContent",
        type: "html",
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
