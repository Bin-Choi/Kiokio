<template>
  <tr class="d-flex">
    <td class="box border" style="width: 5vh">{{ index + 1 }}</td>
    <td class="box border" style="width: 5vh">{{ inbody.grade }}</td>
    <td class="box border" style="width: 5vh">{{ inbody.room }}</td>
    <td class="box border" style="width: 5vh">{{ inbody.number }}</td>
    <td class="box border" style="width: 10vh">{{ inbody.name }}</td>
    <td class="box-width border">{{ inbody.test_date }}</td>
    <td class="box-width border">{{ inbody.height }}</td>
    <td class="box-width border">{{ inbody.age }}</td>
    <td class="box-width border">{{ inbody.weight }}</td>
    <td class="box-width border">{{ inbody.body_mass_index }}</td>
    <td class="box-width border">{{ inbody.percent_body_fat }}</td>
    <td class="box-width border">{{ inbody.total_body_water }}</td>
    <td class="box-width border">{{ inbody.protein }}</td>
    <td class="box-width border">{{ inbody.minerals }}</td>
    <td class="box-width border">{{ inbody.body_fat_mass }}</td>
    <td class="box-width border">{{ inbody.skeletal_muscle_mass }}</td>
    <td class="box-width border">{{ inbody.inbody_score }}</td>
  </tr>
</template>

<script>
export default {
  name: 'AdminInbodyDateReadItem',
  props: {
    inbody: Object,
    index: Number,
  },
}
</script>

<style scoped>
.box {
  background-color: white;
  height: 3vh;
  line-height: 3vh;
}
.box-width {
  background-color: white;
  height: 3vh;
  line-height: 3vh;
  width: 13vh;
}
</style>
