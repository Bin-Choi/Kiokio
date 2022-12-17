<template>
  <div
    class="h-100 d-flex flex-column align-items-center justify-content-between"
  >
    <!-- BACK -->
    <div
      class="w-100 d-flex justify-content-between"
      style="font-size: 4vh; margin: 1.5vh; margin-bottom: 0; padding: 2.2vh"
    >
      <font-awesome-icon
        icon="fa-solid fa-circle-arrow-left"
        @click="$router.push({ name: 'inbodyHistory' })"
      />
      <font-awesome-icon
        icon="fa-solid fa-house"
        @click="$router.push({ name: 'index' })"
      />
    </div>

    <!-- PAGE TITLE -->
    <div class="w-75 title shadow">인바디 등록</div>

    <div
      class="w-75 d-flex justify-content-around align-items-center"
      style="font-size: 3vh"
    >
      {{ student.grade }}학년 {{ student.room }}반 {{ student.name }}

      <button class="orange-btn shadow" @click="submit">완료</button>
    </div>

    <!-- INBODY FORM -->
    <div
      class="w-75 bg-white round shadow"
      style="font-size: 2.3vh; padding: 2.5% 2%; height: 43%"
    >
      <div id="scroll-box" class="container" style="height: 100%">
        <div class="row">
          <p class="col-5">검사일시*</p>
          <input type="date" ref="date" class="round col" />
        </div>

        <div class="row">
          <p class="col-5">키*</p>
          <input
            type="number"
            ref="height"
            @focus="focusChange"
            class="col-4"
            placeholder="필수입력"
          />
          <p class="col-1">cm</p>
        </div>

        <div class="row">
          <p class="col-5">나이*</p>
          <input
            type="number"
            ref="age"
            @focus="focusChange"
            class="col-4"
            placeholder="필수입력"
          />
          <p class="col-1">세</p>
        </div>

        <div class="row">
          <p class="col-5">체중*</p>
          <input
            type="number"
            ref="weight"
            @focus="focusChange"
            class="col-4"
            placeholder="필수입력"
          />
          <p class="col-1">kg</p>
        </div>

        <div class="row">
          <p class="col-5">BMI*</p>
          <input
            type="number"
            ref="bmi"
            @focus="focusChange"
            class="col-4"
            placeholder="필수입력"
          />
          <p class="col-1">kg/m<sup>2</sup></p>
        </div>

        <div class="row">
          <P class="col-5">체지방률*</P>
          <input
            type="number"
            ref="fatpercent"
            @focus="focusChange"
            class="col-4"
            placeholder="필수입력"
          />
          <p class="col-1">%</p>
        </div>

        <div class="row">
          <p class="col-5">체수분</p>
          <input type="text" ref="water" @focus="focusChange" class="col-4" />
          <p class="col-1">L</p>
        </div>

        <div class="row">
          <p class="col-5">단백질</p>
          <input type="text" ref="protein" @focus="focusChange" class="col-4" />
          <p class="col-1">kg</p>
        </div>

        <div class="row">
          <p class="col-5">무기질</p>
          <input
            type="text"
            ref="minerals"
            @focus="focusChange"
            class="col-4"
          />
          <p class="col-1">kg</p>
        </div>

        <div class="row">
          <p class="col-5">체지방량</p>
          <input type="text" ref="fatmass" @focus="focusChange" class="col-4" />
          <p class="col-1">kg</p>
        </div>

        <div class="row">
          <p class="col-5">골격근량</p>
          <input type="text" ref="muscle" @focus="focusChange" class="col-4" />
          <p class="col-1">kg</p>
        </div>

        <div class="row">
          <p class="col-5">인바디점수</p>
          <input type="text" ref="score" @focus="focusChange" class="col-4" />
          <p class="col-1">점</p>
        </div>
      </div>
    </div>

    <the-keypad class="w-100" @input="input" @del="del" />
  </div>
</template>

<script>
import TheKeypad from '../components/TheKeypad.vue'
import axios from 'axios'

export default {
  name: 'InbodyCreateView',
  components: {
    TheKeypad,
  },
  computed: {
    student() {
      return this.$store.state.student
    },
    axios_URL() {
      return this.$store.state.axios_URL
    },
  },
  methods: {
    focusChange(event) {
      this.focusElem = event.target
    },
    input(value) {
      if (this.focusElem.value.length < 5) {
        this.focusElem.value += value
      }
    },
    del() {
      if (this.focusElem.value.length > 0) {
        this.focusElem.value = this.focusElem.value.slice(0, -1)
      }
    },
    submit() {
      console.log(this.$refs.score.value)
      // Data validation
      const regDate = /^\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$/
      const regFloatBlank = /(^\d*$)|(^\d{1,}.\d{1,2}$)/
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

      if (!regFloatBlank.test(this.$refs.fatpercent.value)) {
        alert('체지방률은 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.fatpercent.focus()
        return
      }

      if (!regFloatBlank.test(this.$refs.water.value)) {
        alert('체수분은 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.water.focus()
        return
      }

      if (!regFloatBlank.test(this.$refs.protein.value)) {
        alert('단백질은 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.protein.focus()
        return
      }

      if (!regFloatBlank.test(this.$refs.minerals.value)) {
        alert('무기질은 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.minerals.focus()
        return
      }

      if (!regFloatBlank.test(this.$refs.fatmass.value)) {
        alert('체지방량은 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.fatmass.focus()
        return
      }

      if (!regFloatBlank.test(this.$refs.muscle.value)) {
        alert('골격근량은 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.muscle.focus()
        return
      }

      if (!regFloatBlank.test(this.$refs.score.value)) {
        alert('인바디점수는 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.score.focus()
        return
      }

      axios({
        method: 'post',
        url: `${this.axios_URL}/students/${this.student.id}/inbody/create/`,
        data: {
          password: this.student.password,
          inbody: {
            student: this.student.id,
            height: this.$refs.height.value,
            age: this.$refs.age.value,
            test_date: this.$refs.date.value,
            total_body_water: this.$refs.water.value,
            protein: this.$refs.protein.value,
            minerals: this.$refs.minerals.value,
            body_fat_mass: this.$refs.fatmass.value,
            weight: this.$refs.weight.value,
            skeletal_muscle_mass: this.$refs.muscle.value,
            body_mass_index: this.$refs.bmi.value,
            percent_body_fat: this.$refs.fatpercent.value,
            inbody_score: this.$refs.score.value,
          },
        },
      })
        .then((res) => {
          this.$store.commit('INBODY_INFO', res.data)
          this.$router.push({ name: 'inbodyDetail' })
        })
        .catch((err) => {
          // console.log(err)
          const status = err.response.status

          if (status === 400) {
            alert(`${err.request.responseText}`)
          } else if (status === 401) {
            alert('다시 로그인해주세요')
            this.$router.push({ name: 'inbody' })
          }
        })
    },
  },
  mounted() {
    this.$refs.height.focus()
  },
}
</script>

<style scoped>
.row {
  margin: 1vh 0;
  line-height: 5vh;
}

input {
  margin-right: 1.5vh;
  height: 5vh;
  background: none;
  border: 0.2vh solid #ffa946;
  border-radius: 1vh;
  box-shadow: 0.1vh 0.1vh 0.1vh #ffa94651;
}
</style>
