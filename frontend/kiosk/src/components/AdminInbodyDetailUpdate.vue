<template>
  <div>
    <div>
      <button class="gray-btn" @click="$emit('change-mode-R')">취소</button>
      <button class="blue-btn" @click="updateInbody">저장</button>
    </div>
    <div class="d-flex flex-column" style="overflow-y: scroll">
      <div>{{ student.name }}, {{ student.gender }}</div>
      <div>
        {{ student.grade }}학년 {{ student.room }}반 {{ student.number }}번호
      </div>
      <div
        id="scroll-box"
        class="container"
        style="font-size: 2.5vh; height: 100%">
        <div class="row">
          <p class="col">검사일시</p>
          <input
            type="date"
            ref="date"
            v-model="inbodyCopy.test_date"
            class="rounded col" />
        </div>

        <div class="row">
          <p class="col">키(cm)</p>
          <input
            type="text"
            ref="height"
            v-model="inbodyCopy.height"
            class="rounded col" />
        </div>

        <div class="row">
          <p class="col">나이(세)</p>
          <input
            type="text"
            ref="age"
            v-model="inbodyCopy.age"
            class="rounded col" />
        </div>

        <div class="row">
          <p class="col">체수분(L)</p>
          <input
            type="text"
            ref="water"
            v-model="inbodyCopy.total_body_water"
            class="rounded col" />
        </div>

        <div class="row">
          <p class="col">단백질(kg)</p>
          <input
            type="text"
            ref="protein"
            v-model="inbodyCopy.protein"
            class="rounded col" />
        </div>

        <div class="row">
          <p class="col">무기질(kg)</p>
          <input
            type="text"
            ref="minerals"
            v-model="inbodyCopy.minerals"
            class="rounded col" />
        </div>

        <div class="row">
          <p class="col">체지방량(kg)</p>
          <input
            type="text"
            ref="fatmass"
            v-model="inbodyCopy.body_fat_mass"
            class="rounded col" />
        </div>

        <div class="row">
          <p class="col">체중(kg)</p>
          <input
            type="text"
            ref="weight"
            v-model="inbodyCopy.weight"
            class="rounded col" />
        </div>

        <div class="row">
          <p class="col">골격근량(kg)</p>
          <input
            type="text"
            ref="muscle"
            v-model="inbodyCopy.skeletal_muscle_mass"
            class="rounded col" />
        </div>

        <div class="row">
          <p class="col">BMI(kg/m^2)</p>
          <input
            type="text"
            ref="bmi"
            v-model="inbodyCopy.body_mass_index"
            class="rounded col" />
        </div>

        <div class="row">
          <P class="col">체지방률(%)</P>
          <input
            type="text"
            ref="fatpercent"
            v-model="inbodyCopy.percent_body_fat"
            class="rounded col" />
        </div>

        <div class="row">
          <p class="col">인바디점수(점)</p>
          <input
            type="text"
            ref="score"
            v-model="inbodyCopy.inbody_score"
            class="rounded col" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axiosAuth from '@/axios/axios'

export default {
  name: 'AdminInbodyDetailUpdate',
  props: {
    studentIndex: Number,
    inbodyIndex: Number,
  },
  data() {
    return {
      inbodyCopy: null,
    }
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
  watch: {
    inbody(newInbody) {
      this.inbodyCopy = JSON.parse(JSON.stringify(newInbody))
    },
  },
  mounted() {
    this.inbodyCopy = JSON.parse(JSON.stringify(this.inbody))
  },
  methods: {
    updateInbody() {
      axiosAuth({
        method: 'put',
        url: `${this.axios_URL}/students/inbody/${this.inbodyCopy.id}/admin/`,
        headers: {
          Authorization: `Bearer ${this.access}`,
        },
        data: this.inbodyCopy,
      })
        .then((res) => {
          console.log(res)
          const payload = {
            studentIndex: this.studentIndex,
            inbodyIndex: this.inbodyIndex,
            inbody: this.inbodyCopy,
          }
          this.$store.commit('CHANGE_STUDENT_INBODY_DETAIL', payload)
          this.$emit('change-mode-R')
        })
        .catch((err) => {
          console.error(err)
        })
    },
  },
}
</script>

<style scoped></style>
