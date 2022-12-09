<template>
  <div
    class="h-100 d-flex flex-column align-items-center justify-content-between"
  >
    <!-- BACK -->
    <div
      class="w-100 d-flex justify-content-between"
      style="font-size: 4.5vh; margin: 1.5vh; margin-bottom: 0; padding: 2.2vh"
    >
      <font-awesome-icon
        icon="fa-solid fa-circle-arrow-left"
        @click="$router.go(-1)"
      />
      <font-awesome-icon
        icon="fa-solid fa-house"
        @click="$router.push({ name: 'index' })"
      />
    </div>

    <!-- PAGE TITLE -->
    <div
      class="w-75 bg-primary rounded text-light shadow"
      style="font-size: 5vh"
    >
      인바디 등록
    </div>

    <div style="font-size: 3vh">
      {{ student.grade }}학년 {{ student.room }}반 {{ student.name }}
    </div>

    <!-- INBODY FORM -->
    <div
      class="w-75 bg-light rounded shadow"
      style="font-size: 2.5vh; padding: 2.5% 2%; height: 32%"
    >
      <div id="scroll-box" class="container" style="height: 100%">
        <div class="row">
          <p class="col">검사일시</p>
          <input type="date" ref="date" class="rounded col" />
        </div>

        <div class="row">
          <p class="col">키(cm)</p>
          <input
            type="number"
            ref="height"
            @focus="focusChange"
            @input="(event) => (text = event.target.value)"
            class="rounded col"
          />
        </div>

        <div class="row">
          <p class="col">나이(세)</p>
          <input
            type="number"
            ref="age"
            @focus="focusChange"
            @input="(event) => (text = event.target.value)"
            class="rounded col"
          />
        </div>

        <div class="row">
          <p class="col">체수분(L)</p>
          <input
            type="number"
            ref="water"
            @focus="focusChange"
            @input="(event) => (text = event.target.value)"
            class="rounded col"
          />
        </div>

        <div class="row">
          <p class="col">단백질(kg)</p>
          <input
            type="number"
            ref="protein"
            @focus="focusChange"
            @input="(event) => (text = event.target.value)"
            class="rounded col"
          />
        </div>

        <div class="row">
          <p class="col">무기질(kg)</p>
          <input
            type="number"
            ref="minerals"
            @focus="focusChange"
            @input="(event) => (text = event.target.value)"
            class="rounded col"
          />
        </div>

        <div class="row">
          <p class="col">체지방량(kg)</p>
          <input
            type="number"
            ref="fatmass"
            @focus="focusChange"
            @input="(event) => (text = event.target.value)"
            class="rounded col"
          />
        </div>

        <div class="row">
          <p class="col">체중(kg)</p>
          <input
            type="number"
            ref="weight"
            @focus="focusChange"
            @input="(event) => (text = event.target.value)"
            class="rounded col"
          />
        </div>

        <div class="row">
          <p class="col">골격근량(kg)</p>
          <input
            type="number"
            ref="muscle"
            @focus="focusChange"
            @input="(event) => (text = event.target.value)"
            class="rounded col"
          />
        </div>

        <div class="row">
          <p class="col">BMI(kg/m^2)</p>
          <input
            type="number"
            ref="bmi"
            @focus="focusChange"
            @input="(event) => (text = event.target.value)"
            class="rounded col"
          />
        </div>

        <div class="row">
          <P class="col">체지방률(%)</P>
          <input
            type="number"
            ref="fatpercent"
            @focus="focusChange"
            @input="(event) => (text = event.target.value)"
            class="rounded col"
          />
        </div>

        <div class="row">
          <p class="col">인바디점수(점)</p>
          <input
            type="number"
            ref="score"
            @focus="focusChange"
            @input="(event) => (text = event.target.value)"
            class="rounded col"
          />
        </div>
      </div>
    </div>
    <!-- BUTTON -->
    <button
      type="button"
      class="btn btn-primary shadow"
      style="font-size: 2.5vh"
      @click="submit"
    >
      등록하기
    </button>
    <the-keypad class="w-100 align-self-end" @input="input" @del="del" />
  </div>
</template>

<script>
import TheKeypad from "../components/TheKeypad.vue"
import axios from "axios"

export default {
  name: "InbodyCreateView",
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
      // Check if the data is null
      if (
        !this.$refs.height.value ||
        !this.$refs.age.value ||
        !this.$refs.date.value ||
        !this.$refs.water.value ||
        !this.$refs.protein.value ||
        !this.$refs.minerals.value ||
        !this.$refs.fatmass.value ||
        !this.$refs.weight.value ||
        !this.$refs.muscle.value ||
        !this.$refs.bmi.value ||
        !this.$refs.fatpercent.value ||
        !this.$refs.score.value
      ) {
        alert("정보를 모두 입력해주세요")
        return
      }

      axios({
        method: "post",
        url: `${this.axios_URL}/students/inbody/create/`,
        data: {
          student: this.student.pk,
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
      })
        .then((res) => {
          this.$store.commit("INBODY_INFO", res.data)
          this.$router.push({ name: "inbodyDetail" })
        })
        .catch((err) => {
          console.log(err)
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
}

input {
  margin-right: 1.5vh;
  height: 5vh;
  background: none;
  border: 0.2vh solid #2b64aa1e;
  border-radius: 0.5vh;
  box-shadow: 0.1vh 0.1vh 0.1vh #2b64aa1e;
}
</style>
