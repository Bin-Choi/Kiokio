<template>
  <div>
    <div class="d-flex justify-content-between">
      <div></div>
      <div style="font-size: 2.5vh; font-weight: bold">
        {{ student.grade }}학년 {{ student.room }}반 {{ student.number }}번
        {{ student.name }} ({{ student.gender }})
      </div>
      <div>
        <button class="red-btn" @click="$emit('change-mode-R')">취소</button>
        <button class="blue-btn" @click="updateInbody" style="margin-left: 1vh">
          저장
        </button>
      </div>
    </div>

    <!-- INBODY CONTENT -->
    <div class="w-75 m-auto rounded" style="font-size: 2.5vh; padding: 2vh">
      <div id="admin-scroll-box" class="container">
        <div class="row">
          <p class="col-6">검사일시*</p>
          <input
            type="date"
            ref="date"
            v-model="inbodyCopy.test_date"
            class="rounded shadow-sm col-5" />
        </div>

        <div class="row">
          <p class="col-6">키(cm)*</p>
          <input
            type="number"
            ref="heihgt"
            placeholder="필수입력"
            v-model="inbodyCopy.height"
            class="rounded shadow-sm col-5" />
        </div>

        <div class="row">
          <p class="col-6">나이(세)*</p>
          <input
            type="number"
            ref="age"
            placeholder="필수입력"
            v-model="inbodyCopy.age"
            class="rounded shadow-sm col-5" />
        </div>

        <div class="row">
          <p class="col-6">체중(kg)*</p>
          <input
            type="number"
            ref="weight"
            placeholder="필수입력"
            v-model="inbodyCopy.weight"
            class="rounded shadow-sm col-5" />
        </div>

        <div class="row">
          <p class="col-6">BMI(kg/m^2)*</p>
          <input
            type="number"
            ref="bmi"
            placeholder="필수입력"
            v-model="inbodyCopy.body_mass_index"
            class="rounded shadow-sm col-5" />
        </div>

        <div class="row">
          <P class="col-6">체지방률(%)*</P>
          <input
            type="number"
            ref="fatpercent"
            v-model="inbodyCopy.percent_body_fat"
            class="rounded shadow-sm col-5" />
        </div>

        <div class="row">
          <p class="col-6">체수분(L)</p>
          <input
            type="number"
            ref="water"
            v-model="inbodyCopy.total_body_water"
            class="rounded shadow-sm col-5" />
        </div>

        <div class="row">
          <p class="col-6">단백질(kg)</p>
          <input
            type="number"
            ref="protein"
            v-model="inbodyCopy.protein"
            class="rounded shadow-sm col-5" />
        </div>

        <div class="row">
          <p class="col-6">무기질(kg)</p>
          <input
            type="number"
            ref="minerals"
            v-model="inbodyCopy.minerals"
            class="rounded shadow-sm col-5" />
        </div>

        <div class="row">
          <p class="col-6">체지방량(kg)</p>
          <input
            type="number"
            ref="fatmass"
            v-model="inbodyCopy.body_fat_mass"
            class="rounded shadow-sm col-5" />
        </div>

        <div class="row">
          <p class="col-6">골격근량(kg)</p>
          <input
            type="number"
            ref="muscle"
            v-model="inbodyCopy.skeletal_muscle_mass"
            class="rounded shadow-sm col-5" />
        </div>

        <div class="row">
          <p class="col-6">인바디점수(점)</p>
          <input
            type="number"
            ref="score"
            v-model="inbodyCopy.inbody_score"
            class="rounded shadow-sm col-5" />
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
      // 입력값 유효성 검사
      const regDate = /^\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$/
      const regFloat = /(^\d+$)|(^\d{1,}.\d{1,2}$)/
      const regFloatBlank = /(^\d*$)|(^\d{1,}.\d{1,2}$)/
      const regInt = /^[0-9]+$/

      if (!regDate.test(this.inbodyCopy.test_date)) {
        alert('검사일을 입력해주세요.')
        this.$refs.date.focus()
        return
      }

      if (!regFloat.test(this.inbodyCopy.height)) {
        alert('키는 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.height.focus()
        return
      }

      if (!regInt.test(this.inbodyCopy.age)) {
        alert('나이를 정확히 입력해주세요.')
        this.$refs.age.focus()
        return
      }

      if (!regFloat.test(this.inbodyCopy.weight)) {
        alert('체중은 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.weight.focus()
        return
      }

      if (!regFloat.test(this.inbodyCopy.body_mass_index)) {
        alert('BMI은 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.bmi.focus()
        return
      }

      if (
        this.$refs.fatpercent &&
        !regFloatBlank.test(this.inbodyCopy.percent_body_fat)
      ) {
        alert('체지방률은 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.fatpercent.focus()
        return
      }

      if (
        this.inbodyCopy.tatal_body_water &&
        !regFloatBlank.test(this.inbodyCopy.tatal_body_water)
      ) {
        alert('체수분은 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.water.focus()
        return
      }

      if (
        this.inbodyCopy.protein &&
        !regFloatBlank.test(this.inbodyCopy.protein)
      ) {
        alert('단백질은 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.protein.focus()
        return
      }

      if (
        this.inbodyCopy.minerals &&
        !regFloatBlank.test(this.inbodyCopy.minerals)
      ) {
        alert('무기질은 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.minerals.focus()
        return
      }

      if (
        this.inbodyCopy.body_fat_mass &&
        !regFloatBlank.test(this.inbodyCopy.body_fat_mass)
      ) {
        alert('체지방량은 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.fatmass.focus()
        return
      }

      if (
        this.inbodyCopy.skeletal_muscle_mass &&
        !regFloatBlank.test(this.inbodyCopy.skeletal_muscle_mass)
      ) {
        alert('골격근량은 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.muscle.focus()
        return
      }

      if (
        this.inbodyCopy.inbody_score &&
        !regFloatBlank.test(this.inbodyCopy.inbody_score)
      ) {
        alert('인바디점수는 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.score.focus()
        return
      }

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

<style scoped>
.row p {
  font-weight: bold;
}
.row {
  margin-bottom: 1vh;
}

input {
  border: 0.5vh solid rgba(129, 160, 187, 0.294);
}
</style>
