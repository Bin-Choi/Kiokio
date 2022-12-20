<template>
  <tr class="d-flex">
    <td class="box border attendance-column">학년</td>
    <td class="box border attendance-column">반</td>
    <td class="box border attendance-column">번호</td>
    <td class="box border name-column">이름</td>
    <td
      v-for="day in Array(days)
        .fill()
        .map((v, i) => i + 1)"
      :key="day"
      class="box border attendance-column">
      {{ day }}
    </td>
  </tr>
</template>

<script>
export default {
  name: 'AttendanceTableColumn',
  props: {
    days: Number,
  },
}
</script>

<style scoped>
.box {
  background-color: rgb(240, 240, 240);
}
.name-column {
  width: 10vw;
  min-width: 60px;
}
.attendance-column {
  width: 5vw;
  min-width: 40px;
}
</style>
