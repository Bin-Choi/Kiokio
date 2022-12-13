<template>
  <div>
    <div class="box border">{{ index + 1 }}</div>
    <div class="box border">{{ inbody.test_date }}</div>
    <div class="box border">{{ inbody.height }}</div>
    <div class="box border">{{ inbody.age }}</div>
    <div class="box border">{{ inbody.weight }}</div>
    <div class="box border">{{ inbody.body_mass_index }}</div>
    <div class="box border">{{ inbody.percent_body_fat }}</div>
    <div class="box border">{{ inbody.total_body_water }}</div>
    <div class="box border">{{ inbody.protein }}</div>
    <div class="box border">{{ inbody.minerals }}</div>
    <div class="box border">{{ inbody.body_fat_mass }}</div>
    <div class="box border">{{ inbody.skeletal_muscle_mass }}</div>
    <div class="box border">{{ inbody.inbody_score }}</div>
  </div>
</template>

<script>
export default {
  name: 'AdminInbodyStudentReadItem',
  props: {
    inbody: Object,
    index: Number,
  },
}
</script>

<style scoped>
.box {
  background-color: white;
  height: 30px;
}
</style>
