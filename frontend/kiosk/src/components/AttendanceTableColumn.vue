<template>
  <div class="d-flex">
    <div class="box border name-column">이름</div>
    <div class="box border attendance-column">학년</div>
    <div class="box border attendance-column">반</div>
    <div class="box border attendance-column">번호</div>
    <div
      v-for="day in Array(days)
        .fill()
        .map((v, i) => i + 1)"
      :key="day"
      class="box border attendance-column">
      {{ day }}
    </div>
  </div>
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
  background-color: white;
}
.name-column {
  width: 15vw;
  min-width: 60px;
}
.attendance-column {
  width: 10vw;
  min-width: 40px;
}
</style>
