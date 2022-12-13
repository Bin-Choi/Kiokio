<template>
  <div>
    <div class="d-flex justify-content-between">
      <div></div>
      <div style="margin-bottom: 2vh; font-size: 2.5vh; font-weight: bold">
        {{ student.grade }}학년 {{ student.room }}반 {{ student.number }}번

        {{ student.name }} ({{ student.gender }})
      </div>
      <div>
        <button class="blue-btn shadow-sm" @click="$emit('change-mode-U')">
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
    <div class="w-75 m-auto rounded" style="font-size: 2.3vh; padding: 2vh">
      <div id="admin-scroll-box" class="container">
        <div class="row">
          <p class="col-6">검사일시</p>
          <div class="col-5 rounded shadow-sm">{{ inbody.test_date }}</div>
        </div>

        <div class="row">
          <p class="col-6">키</p>
          <div class="col-5 rounded shadow-sm">{{ inbody.height }} cm</div>
        </div>

        <div class="row">
          <p class="col-6">나이(세)</p>
          <div class="col-5 rounded shadow-sm">{{ inbody.age }} 세</div>
        </div>

        <div class="row">
          <p class="col-6">체중</p>
          <div class="col-5 rounded shadow-sm">{{ inbody.weight }} kg</div>
        </div>

        <div class="row">
          <p class="col-6">BMI</p>
          <div class="col-5 rounded shadow-sm">
            {{ inbody.body_mass_index }} kg/m^2
          </div>
        </div>

        <div class="row">
          <p class="col-6">체지방률</p>
          <div class="col-5 rounded shadow-sm">
            {{ inbody.percent_body_fat }} %
          </div>
        </div>

        <div class="row">
          <p class="col-6">체수분</p>
          <div class="col-5 rounded shadow-sm">
            {{ inbody.total_body_water }} L
          </div>
        </div>

        <div class="row">
          <p class="col-6">단백질</p>
          <div class="col-5 rounded shadow-sm">{{ inbody.protein }} kg</div>
        </div>

        <div class="row">
          <p class="col-6">무기질</p>
          <div class="col-5 rounded shadow-sm">{{ inbody.minerals }} kg</div>
        </div>

        <div class="row">
          <p class="col-6">체지방량</p>
          <div class="col-5 rounded shadow-sm">
            {{ inbody.body_fat_mass }} kg
          </div>
        </div>

        <div class="row">
          <p class="col-6">골격근량</p>
          <div class="col-5 rounded shadow-sm">
            {{ inbody.skeletal_muscle_mass }} kg
          </div>
        </div>

        <div class="row">
          <p class="col-6">인바디 점수</p>
          <div class="col-5 rounded shadow-sm">
            {{ inbody.inbody_score }} 점
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axiosAuth from '@/axios/axios'

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
  },
}
</script>

<style scoped>
.row p {
  font-weight: bold;
}
.row {
  margin-bottom: 1vh;
}

.row div {
  background-color: white;
  border: 0.5vh solid rgba(129, 160, 187, 0.294);
}
</style>
