<template>
  <tr>
    <td class="box border">{{ index + 1 }}</td>
    <td class="box border">{{ inbody.test_date }}</td>
    <td class="box border">{{ inbody.height }}</td>
    <td class="box border">{{ inbody.age }}</td>
    <td class="box border">{{ inbody.weight }}</td>
    <td class="box border">{{ inbody.body_mass_index }}</td>
    <td class="box border">{{ inbody.percent_body_fat }}</td>
    <td class="box border">{{ inbody.total_body_water }}</td>
    <td class="box border">{{ inbody.protein }}</td>
    <td class="box border">{{ inbody.minerals }}</td>
    <td class="box border">{{ inbody.body_fat_mass }}</td>
    <td class="box border">{{ inbody.skeletal_muscle_mass }}</td>
    <td class="box border">{{ inbody.inbody_score }}</td>
  </tr>
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
  height: 4.5vh;
  line-height: 4.5vh;
  width: 15vh;
}
tr {
  display: block;
  float: left;
}
td {
  display: block;
}
</style>
