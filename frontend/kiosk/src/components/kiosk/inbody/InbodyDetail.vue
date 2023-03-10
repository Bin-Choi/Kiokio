<template>
  <div
    class="w-75 bg-white round shadow"
    style="padding: 1.5vh 1vh; height: 60vh"
  >
    <div
      id="scroll-box"
      class="container"
      style="font-size: 2.5vh; height: 100%"
    >
      <div class="row">
        <p class="col-5">검사일시</p>
        <div class="col-6">{{ inbody.test_date }}</div>
      </div>

      <div class="row">
        <p class="col-5">키</p>
        <div class="col-4">{{ inbody.height }}</div>
        <p class="col-1">cm</p>
      </div>

      <div class="row">
        <p class="col-5">나이</p>
        <div class="col-4">{{ inbody.age }}</div>
        <p class="col-1">세</p>
      </div>

      <div class="row">
        <p class="col-5">체중</p>
        <div class="col-4">{{ inbody.weight }}</div>
        <p class="col-1">kg</p>
      </div>

      <div class="row">
        <p class="col-5">BMI</p>
        <div class="col-4">{{ inbody.body_mass_index }}</div>
        <p class="col-1">kg/m<sup>2</sup></p>
      </div>

      <div class="row">
        <p class="col-5">체지방률</p>
        <div class="col-4">{{ inbody.percent_body_fat }}</div>
        <p class="col-1">%</p>
      </div>

      <div class="row">
        <p class="col-5">체수분</p>
        <div class="col-4">{{ inbody.total_body_water }}</div>
        <p class="col-1">L</p>
      </div>

      <div class="row">
        <p class="col-5">단백질</p>
        <div class="col-4">{{ inbody.protein }}</div>
        <p class="col-1">kg</p>
      </div>

      <div class="row">
        <p class="col-5">무기질</p>
        <div class="col-4">{{ inbody.minerals }}</div>
        <p class="col-1">kg</p>
      </div>

      <div class="row">
        <p class="col-5">체지방량</p>
        <div class="col-4">{{ inbody.body_fat_mass }}</div>
        <p class="col-1">kg</p>
      </div>

      <div class="row">
        <p class="col-5">골격근량</p>
        <div class="col-4">{{ inbody.skeletal_muscle_mass }}</div>
        <p class="col-1">kg</p>
      </div>

      <div class="row">
        <p class="col-5">인바디점수</p>
        <div class="col-4">{{ inbody.inbody_score }}</div>
        <p class="col-1">점</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'InbodyDetail',
  computed: {
    inbody() {
      return this.$store.state.inbody
    },
  },
}
</script>

<style scoped>
.row {
  margin: 1vh 0;
  line-height: 5vh;
}

.row div {
  height: 5vh;
  background: none;
  border: 0.2vh solid #ffa946;
  border-radius: 1vh;
  box-shadow: 0.1vh 0.1vh 0.1vh #ffa94651;
  font-size: 2.3vh;
}
</style>
