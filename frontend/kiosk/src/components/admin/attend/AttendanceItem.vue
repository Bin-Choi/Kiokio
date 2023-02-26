<template>
  <tr :id="`student-${student.id}`" class="d-flex">
    <td class="box border attendance-column">{{ student.grade }}</td>
    <td class="box border attendance-column">{{ student.room }}</td>
    <td class="box border attendance-column">{{ student.number }}</td>
    <td class="box border name-column">{{ student.name }}</td>
    <td
      v-for="day in Array(days)
        .fill()
        .map((v, i) => i + 1)"
      :key="day"
      class="box border attendance-column"></td>
  </tr>
</template>

<script>
export default {
  name: 'AttendanceItem',
  props: {
    student: Object,
    days: Number,
  },
  watch: {
    // 학생이나 검색날짜가 바뀌면 allocAttendance() 재실행
    student() {
      this.allocAttendance()
    },
    days() {
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
      // 모든 div 태그 초기화
      for (let i; i < this.days; i++) {
        divs[3 + i].innerText = null
      }
      // 출석시간 담기
      for (const attendance of this.student.attendance_set) {
        // 날짜 정보 추출
        const day = parseInt(attendance.date.slice(-2))
        // 해당 날짜 div태그에 시간을 추가
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
  width: 10vw;
  min-width: 60px;
}
.attendance-column {
  width: 5vw;
  min-width: 40px;
}
</style>
