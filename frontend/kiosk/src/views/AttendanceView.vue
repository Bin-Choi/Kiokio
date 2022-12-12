<template>
  <div
    class="d-flex flex-column align-items-center"
    style="width: 100vw; height: 100vh; padding: 7vh">
    <AdminHeader />

    <div
      class="bg-secondary rounded shadow d-flex flex-column"
      style="width: 100%; height: 80vh; padding: 3vh; margin-top: 5vh">
      <AttendanceHeader
        @search-by-class="searchByClass"
        @search-by-name="searchByName" />
      <div v-if="students" style="overflow-x: scroll; overflow-y: scroll">
        <AttendanceTableColumn :days="days" />
        <AttendanceItem
          v-for="student in students"
          :key="student.id"
          :student="student"
          :days="days" />
      </div>
    </div>
  </div>
</template>

<script>
import AdminHeader from '@/components/AdminHeader.vue'
import AttendanceHeader from '@/components/AttendanceHeader.vue'
import AttendanceTableColumn from '@/components/AttendanceTableColumn.vue'
import AttendanceItem from '@/components/AttendanceItem.vue'
import axiosAuth from '@/axios/axios'

const daysOfMonth = {
  1: 31,
  2: 28,
  3: 31,
  4: 30,
  5: 31,
  6: 30,
  7: 31,
  8: 31,
  9: 30,
  10: 31,
  11: 30,
  12: 31,
}

export default {
  name: 'AttendanceView',
  components: {
    AdminHeader,
    AttendanceHeader,
    AttendanceTableColumn,
    AttendanceItem,
  },
  data() {
    return {
      year: 22,
      month: 12,
      students: null,
    }
  },
  computed: {
    axios_URL() {
      return this.$store.state.axios_URL
    },
    access() {
      return this.$store.state.access
    },
    days() {
      const year = parseInt(this.year)
      const month = parseInt(this.month)
      if (
        month == 2 &&
        (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0))
      ) {
        return 29
      } else {
        return daysOfMonth[`${month}`]
      }
    },
  },
  methods: {
    // Read
    searchByClass(year, month, grade, room) {
      this.year = year
      this.month = month
      const url = `${this.axios_URL}/students/${year}/${month}/${grade}/${room}/attendance/`
      this.searchStudent(url)
    },
    searchByName(year, month, name) {
      this.year = year
      this.month = month
      const url = `${this.axios_URL}/students/${year}/${month}/${name}/attendance/`
      this.searchStudent(url)
    },
    searchStudent(url) {
      axiosAuth({
        method: 'get',
        url: url,
        headers: {
          Authorization: `Bearer ${this.access}`,
        },
      })
        .then((res) => {
          console.log(res)
          this.students = res.data
        })
        .catch((err) => {
          console.error(err)
          alert('해당 정보의 학생이 존재하지 않습니다')
        })
    },
  },
}
</script>

<style>
.green-btn {
  background-color: rgb(109, 163, 28);
  width: 10vw;
  height: 5vh;
  border-radius: 1vh;

  border: 0;
  outline: 0;

  color: white;
  font-size: 2vh;
  font-weight: bold;
}
.green-btn:focus {
  outline: 2px solid black;
}
.green-btn:hover {
  background-color: rgb(13, 81, 17);
}
.red-btn {
  background-color: rgb(193, 32, 42);
  width: 10vw;
  height: 5vh;
  border-radius: 1vh;

  border: 0;
  outline: 0;

  color: white;
  font-size: 2vh;
  font-weight: bold;
}
.red-btn:focus {
  outline: 2px solid black;
}
.red-btn:hover {
  background-color: rgb(123, 18, 18);
}
.blue-btn {
  background-color: rgb(30, 30, 148);
  width: 10vw;
  height: 5vh;
  border-radius: 1vh;

  border: 0;
  outline: 0;

  color: white;
  font-size: 2vh;
  font-weight: bold;
}
.blue-btn:focus {
  outline: 2px solid black;
}
.blue-btn:hover {
  background-color: rgb(18, 28, 115);
}
</style>
