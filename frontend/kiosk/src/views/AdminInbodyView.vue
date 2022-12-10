<template>
  <div
    class="d-flex flex-column align-items-center"
    style="width: 100vw; height: 100vh; padding: 7vh">
    <AdminHeader />

    <div
      class="bg-secondary rounded shadow d-flex flex-column"
      style="width: 100%; height: 80vh; padding: 3vh; margin-top: 5vh">
      <div v-if="mode === 'Default'">
        <AdminInbodyHeader
          @search-by-class="searchByClass"
          @search-by-name="searchByName" />
        <div
          v-if="inbodyStudents"
          style="overflow-x: scroll; overflow-y: scroll">
          <AdminInbodyItem
            v-for="(student, index) in inbodyStudents"
            :key="student.id"
            :student="student"
            :index="index"
            @change-mode-student="changeModeStudent"
            @change-mode-detail="changeModeDetail" />
        </div>
      </div>
      <div v-if="mode === 'Student' && student">
        <AdminInbodyStudent
          :studentIndex="studentIndex"
          @change-mode-default="changeModeDefault" />
      </div>
      <div v-if="mode === 'Detail' && inbody">
        <AdminInbodyDetail
          :studentIndex="studentIndex"
          :inbodyIndex="inbodyIndex"
          @change-mode-default="changeModeDefault" />
      </div>
    </div>
  </div>
</template>

<script>
import AdminHeader from '@/components/AdminHeader.vue'
import AdminInbodyHeader from '@/components/AdminInbodyHeader.vue'
import AdminInbodyItem from '@/components/AdminInbodyItem.vue'
import AdminInbodyStudent from '@/components/AdminInbodyStudent.vue'
import AdminInbodyDetail from '@/components/AdminInbodyDetail.vue'
import axios from 'axios'

export default {
  name: 'AdminInbodyView',
  components: {
    AdminHeader,
    AdminInbodyHeader,
    AdminInbodyItem,
    AdminInbodyStudent,
    AdminInbodyDetail,
  },
  data() {
    return {
      mode: 'Default',
      student: null,
      inbody: null,
      studentIndex: null,
      inbodyIndex: null,
    }
  },
  computed: {
    axios_URL() {
      return this.$store.state.axios_URL
    },
    access() {
      return this.$store.state.access
    },
    inbodyStudents() {
      return this.$store.state.inbodyStudents
    },
  },
  methods: {
    // Read
    searchByClass(grade, room) {
      const url = `${this.axios_URL}/students/${grade}/${room}/inbody/admin/`
      this.searchStudent(url)
    },
    searchByName(name) {
      const url = `${this.axios_URL}/students/${name}/inbody/admin/`
      this.searchStudent(url)
    },
    searchStudent(url) {
      axios({
        method: 'get',
        url: url,
        headers: {
          Authorization: `Bearer ${this.access}`,
        },
      })
        .then((res) => {
          console.log(res)
          this.$store.commit('SAVE_INBODY_STUDENTS', res.data)
        })
        .catch((err) => {
          console.error(err)
          alert('해당 정보의 학생이 존재하지 않습니다')
        })
    },
    //change mode
    changeModeDefault() {
      this.mode = 'Default'
    },
    changeModeStudent(studentIndex) {
      this.mode = 'Student'
      this.studentIndex = studentIndex
      this.student = this.inbodyStudents[studentIndex]
    },
    changeModeDetail(studentIndex, inbodyIndex) {
      this.mode = 'Detail'
      this.studentIndex = studentIndex
      this.inbodyIndex = inbodyIndex
      this.student = {
        name: this.inbodyStudents[studentIndex].name,
        grade: this.inbodyStudents[studentIndex].grade,
        room: this.inbodyStudents[studentIndex].room,
        number: this.inbodyStudents[studentIndex].number,
        gender: this.inbodyStudents[studentIndex].gender,
      }
      this.inbody = this.inbodyStudents[studentIndex].inbody_set[inbodyIndex]
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
.gray-btn {
  background-color: rgb(121, 121, 121);
  width: 10vw;
  height: 5vh;
  border-radius: 1vh;

  border: 0;
  outline: 0;

  color: white;
  font-size: 2vh;
  font-weight: bold;
}
.gray-btn:focus {
  outline: 2px solid black;
}
.gray-btn:hover {
  background-color: rgb(66, 66, 66);
}
</style>
