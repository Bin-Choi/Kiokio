<template>
  <div :id="`student-${student.id}`" class="d-flex">
    <div class="box border name-column">{{ student.name }}</div>
    <div class="box border attendance-column">{{ student.grade }}</div>
    <div class="box border attendance-column">{{ student.room }}</div>
    <div class="box border attendance-column">{{ student.number }}</div>
    <div
      v-for="day in Array(days)
        .fill()
        .map((v, i) => i + 1)"
      :key="day"
      class="box border attendance-column"></div>
  </div>
</template>

<script>
export default {
  name: 'AttendanceItem',
  props: {
    student: Object,
    days: Number,
  },
  watch: {
    student() {
      const divs = document
        .getElementById(`student-${this.student.id}`)
        .children.splice(4)
      for (const div of divs) {
        div.innerText = null
      }
      this.allocAttendance()
    },
  },
  mounted() {
    this.allocAttendance()
  },
  methods: {
    allocAttendance() {
      const divs = document.getElementById(
        `student-${this.student.id}`
      ).children
      for (const attendance of this.student.attendance_set) {
        const day = parseInt(attendance.date.slice(-2))
        let innerText = divs[3 + day].innerText
        innerText = innerText + '\n' + attendance.time.slice(0, 5)
        divs[3 + day].innerText = innerText.trim()
      }
    },
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
