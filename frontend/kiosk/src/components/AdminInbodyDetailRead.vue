<template>
  <div>
    <div class="d-flex justify-content-end" style="margin-bottom: 1vh">
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
    <div class="d-flex flex-column" style="height: 60vh; overflow-y: scroll">
      <div>{{ student.name }}, {{ student.gender }}</div>
      <div>
        {{ student.grade }}학년 {{ student.room }}반 {{ student.number }}번호
      </div>
      <div class="container" style="font-size: 2.5vh; height: 100%">
        <div class="row">
          <p class="col">검사일시</p>
          <div class="col">{{ inbody.test_date }}</div>
        </div>

        <div class="row">
          <p class="col">키</p>
          <div class="col">{{ inbody.height }} cm</div>
        </div>

        <div class="row">
          <p class="col">나이</p>
          <div class="col">{{ inbody.age }} 세</div>
        </div>

        <div class="row">
          <p class="col">체수분</p>
          <div class="col">{{ inbody.total_body_water }} L</div>
        </div>

        <div class="row">
          <p class="col">단백질</p>
          <div class="col">{{ inbody.protein }} kg</div>
        </div>

        <div class="row">
          <p class="col">무기질</p>
          <div class="col">{{ inbody.minerals }} kg</div>
        </div>

        <div class="row">
          <p class="col">체지방량</p>
          <div class="col">{{ inbody.body_fat_mass }} kg</div>
        </div>

        <div class="row">
          <p class="col">체중</p>
          <div class="col">{{ inbody.weight }} kg</div>
        </div>

        <div class="row">
          <p class="col">골격근량</p>
          <div class="col">{{ inbody.skeletal_muscle_mass }} kg</div>
        </div>

        <div class="row">
          <p class="col">BMI</p>
          <div class="col">{{ inbody.body_mass_index }} kg/m^2</div>
        </div>

        <div class="row">
          <p class="col">체지방률</p>
          <div class="col">{{ inbody.percent_body_fat }} %</div>
        </div>

        <div class="row">
          <p class="col">인바디 점수</p>
          <div class="col">{{ inbody.inbody_score }} 점</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

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
      axios({
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

<style scoped></style>
