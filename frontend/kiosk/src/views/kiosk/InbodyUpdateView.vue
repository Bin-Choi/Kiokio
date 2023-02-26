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
        @click="$router.push({ name: 'inbodyDetail' })"
      />
      <font-awesome-icon
        icon="fa-solid fa-house"
        @click="$router.push({ name: 'index' })"
      />
    </div>

    <!-- PAGE TITLE -->
    <div class="w-75 title shadow">인바디 수정</div>

    <div
      class="w-75 d-flex justify-content-around align-items-center"
      style="font-size: 3vh"
    >
      {{ student.grade }}학년 {{ student.room }}반 {{ student.name }}

      <!-- BUTTON -->
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
          <input type="date" ref="date" :value="inbody.test_date" class="col" />
        </div>

        <div class="row">
          <p class="col-5">키*</p>
          <input
            type="text"
            ref="height"
            @focus="focusChange"
            :value="inbody.height"
            class="col-4"
            placeholder="필수입력"
          />
          <div class="col-1">cm</div>
        </div>

        <div class="row">
          <p class="col-5">나이*</p>
          <input
            type="text"
            ref="age"
            @focus="focusChange"
            :value="inbody.age"
            class="col-4"
            placeholder="필수입력"
          />
          <div class="col-1">세</div>
        </div>

        <div class="row">
          <p class="col-5">체중*</p>
          <input
            type="text"
            ref="weight"
            @focus="focusChange"
            :value="inbody.weight"
            class="col-4"
            placeholder="필수입력"
          />
          <div class="col-1">kg</div>
        </div>

        <div class="row">
          <p class="col-5">BMI*</p>
          <input
            type="text"
            ref="bmi"
            @focus="focusChange"
            :value="inbody.body_mass_index"
            class="col-4"
            placeholder="필수입력"
          />
          <div class="col-1">kg/m<sup>2</sup></div>
        </div>

        <div class="row">
          <P class="col-5">체지방률*</P>
          <input
            type="text"
            ref="fatpercent"
            @focus="focusChange"
            :value="inbody.percent_body_fat"
            class="col-4"
            placeholder="필수입력"
          />
          <div class="col-1" c>%</div>
        </div>

        <div class="row">
          <p class="col-5">체수분</p>
          <input
            type="text"
            ref="water"
            @focus="focusChange"
            :value="inbody.total_body_water"
            class="col-4"
          />
          <div class="col-1">L</div>
        </div>

        <div class="row">
          <p class="col-5">단백질</p>
          <input
            type="text"
            ref="protein"
            @focus="focusChange"
            :value="inbody.protein"
            class="col-4"
          />
          <div class="col-1">kg</div>
        </div>

        <div class="row">
          <p class="col-5">무기질</p>
          <input
            type="text"
            ref="minerals"
            @focus="focusChange"
            :value="inbody.minerals"
            class="col-4"
          />
          <div class="col-1">kg</div>
        </div>

        <div class="row">
          <p class="col-5">체지방량</p>
          <input
            type="text"
            ref="fatmass"
            @focus="focusChange"
            :value="inbody.body_fat_mass"
            class="col-4"
          />
          <div class="col-1">kg</div>
        </div>

        <div class="row">
          <p class="col-5">골격근량</p>
          <input
            type="text"
            ref="muscle"
            @focus="focusChange"
            :value="inbody.skeletal_muscle_mass"
            class="col-4"
          />
          <div class="col-1">kg</div>
        </div>

        <div class="row">
          <p class="col-5">인바디점수</p>
          <input
            type="text"
            ref="score"
            @focus="focusChange"
            :value="inbody.inbody_score"
            class="col-4"
          />
          <div class="col-1">점</div>
        </div>
      </div>
    </div>

    <!-- KEYPAD -->
    <the-keypad class="w-100" @input="input" @del="del" />
  </div>
</template>

<script>
// import TheKeypad from '@/components/TheKeypad.vue'
import TheKeypad from '@/components/kiosk/common/TheKeypad.vue'
import axios from 'axios'

export default {
  name: 'InbodyUpdateView',
  components: {
    TheKeypad,
  },
  computed: {
    inbody() {
      return this.$store.state.inbody
    },
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

      if (
        this.$refs.fatpercent.value &&
        !regFloatBlank.test(this.$refs.fatpercent.value)
      ) {
        alert('체지방률은 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.fatpercent.focus()
        return
      }

      if (
        this.$refs.water.value &&
        !regFloatBlank.test(this.$refs.water.value)
      ) {
        alert('체수분은 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.water.focus()
        return
      }

      if (
        this.$refs.protein.value &&
        !regFloatBlank.test(this.$refs.protein.value)
      ) {
        alert('단백질은 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.protein.focus()
        return
      }

      if (
        this.$refs.minerals.value &&
        !regFloatBlank.test(this.$refs.minerals.value)
      ) {
        alert('무기질은 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.minerals.focus()
        return
      }

      if (
        this.$refs.fatmass.value &&
        !regFloatBlank.test(this.$refs.fatmass.value)
      ) {
        alert('체지방량은 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.fatmass.focus()
        return
      }

      if (
        this.$refs.muscle.value &&
        !regFloatBlank.test(this.$refs.muscle.value)
      ) {
        alert('골격근량은 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.muscle.focus()
        return
      }

      if (
        this.$refs.score.value &&
        !regFloatBlank.test(this.$refs.score.value)
      ) {
        alert('인바디점수는 소수점 둘째자리까지 입력가능합니다.')
        this.$refs.score.focus()
        return
      }

      axios({
        method: 'put',
        url: `${this.axios_URL}/students/${this.student.id}/inbody/${this.inbody.id}/`,
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
          console.log(err)
          const {
            response: { status },
          } = err
          if (status === 400) {
            alert(`${err.request.responseText}`)
          } else if (status === 401) {
            alert('다시 로그인해주세요')
            this.$router.push({ name: 'inbody' })
          }
        })
    },
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
