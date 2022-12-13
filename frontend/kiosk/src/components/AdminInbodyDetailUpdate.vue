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
            class="rounded shadow-sm col-5"
          />
        </div>

        <div class="row">
          <p class="col-6">키(cm)*</p>
          <input
            type="text"
            placeholder="필수입력"
            ref="height"
            v-model="inbodyCopy.height"
            class="rounded shadow-sm col-5"
          />
        </div>

        <div class="row">
          <p class="col-6">나이(세)*</p>
          <input
            type="text"
            placeholder="필수입력"
            ref="age"
            v-model="inbodyCopy.age"
            class="rounded shadow-sm col-5"
          />
        </div>

        <div class="row">
          <p class="col-6">체중(kg)*</p>
          <input
            type="text"
            placeholder="필수입력"
            ref="weight"
            v-model="inbodyCopy.weight"
            class="rounded shadow-sm col-5"
          />
        </div>

        <div class="row">
          <p class="col-6">BMI(kg/m^2)*</p>
          <input
            type="text"
            placeholder="필수입력"
            ref="bmi"
            v-model="inbodyCopy.body_mass_index"
            class="rounded shadow-sm col-5"
          />
        </div>

        <div class="row">
          <P class="col-6">체지방률(%)*</P>
          <input
            type="text"
            ref="fatpercent"
            v-model="inbodyCopy.percent_body_fat"
            class="rounded shadow-sm col-5"
          />
        </div>

        <div class="row">
          <p class="col-6">체수분(L)</p>
          <input
            type="text"
            ref="water"
            v-model="inbodyCopy.total_body_water"
            class="rounded shadow-sm col-5"
          />
        </div>

        <div class="row">
          <p class="col-6">단백질(kg)</p>
          <input
            type="text"
            ref="protein"
            v-model="inbodyCopy.protein"
            class="rounded shadow-sm col-5"
          />
        </div>

        <div class="row">
          <p class="col-6">무기질(kg)</p>
          <input
            type="text"
            ref="minerals"
            v-model="inbodyCopy.minerals"
            class="rounded shadow-sm col-5"
          />
        </div>

        <div class="row">
          <p class="col-6">체지방량(kg)</p>
          <input
            type="text"
            ref="fatmass"
            v-model="inbodyCopy.body_fat_mass"
            class="rounded shadow-sm col-5"
          />
        </div>

        <div class="row">
          <p class="col-6">골격근량(kg)</p>
          <input
            type="text"
            ref="muscle"
            v-model="inbodyCopy.skeletal_muscle_mass"
            class="rounded shadow-sm col-5"
          />
        </div>

        <div class="row">
          <p class="col-6">인바디점수(점)</p>
          <input
            type="text"
            ref="score"
            v-model="inbodyCopy.inbody_score"
            class="rounded shadow-sm col-5"
          />
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

      const regFloatNull = /(^\d*$)|(^\d{1,}.\d{1,2}$)/
      const regFloat = /(^\d+$)|(^\d{1,}.\d{1,2}$)/
      const regInt = /^[0-9]+$/

      if (!regDate.test(this.$refs.date.value)) {
        alert('검사일을 입력해주세요.')
        return
      }

      if (!regFloat.test(this.$refs.height.value)) {
        alert('키는 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.height.focus()
        return
      }

      if (!regInt.test(this.$refs.age.value)) {
        alert('나이를 정확히 입력해주세요.')
        this.$refs.age.focus()
        return
      }

      if (!regFloat.test(this.$refs.weight.value)) {
        alert('체중은 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.weight.focus()
        return
      }

      if (!regFloat.test(this.$refs.bmi.value)) {
        alert('BMI은 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.bmi.focus()
        return
      }

      if (!regFloatNull.test(this.$refs.fatpercent.value)) {
        alert('체지방률은 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.fatpercent.focus()
        return
      }

      if (!regFloatNull.test(this.$refs.water.value)) {
        alert('체수분은 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.water.focus()
        return
      }

      if (!regFloatNull.test(this.$refs.protein.value)) {
        alert('단백질은 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.protein.focus()
        return
      }

      if (!regFloatNull.test(this.$refs.minerals.value)) {
        alert('무기질은 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.minerals.focus()
        return
      }

      if (!regFloatNull.test(this.$refs.fatmass.value)) {
        alert('체지방량은 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.fatmass.focus()
        return
      }

      if (!regFloatNull.test(this.$refs.muscle.value)) {
        alert('골격근량은 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.muscle.focus()
        return
      }

      if (!regFloatNull.test(this.$refs.score.value)) {
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
