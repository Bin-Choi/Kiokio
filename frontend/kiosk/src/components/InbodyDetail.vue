<template>
  <div
    class="w-75 bg-light rounded shadow"
    style="padding: 2.5vh 2vh; height: 60vh"
  >
    <div
      id="scroll-box"
      class="container"
      style="font-size: 2.5vh; height: 100%"
    >
      <div class="row">
        <p class="col">검사일시</p>
        <div class="col"></div>
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
}

.row div {
  margin-right: 1.5vh;
  height: 5vh;
  background: none;
  border: 0.2vh solid #2b64aa1e;
  border-radius: 0.5vh;
  box-shadow: 0.1vh 0.1vh 0.1vh #2b64aa1e;
}
</style>
