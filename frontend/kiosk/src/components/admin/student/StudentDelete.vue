<template>
  <div>
    <div class="d-flex justify-content-between">
      <TheButton
        :text="'취소'"
        :onClick="() => $router.push({ name: 'student' })"
      />
      <TheButton :text="'확인'" :onClick="deleteStudent" />
    </div>

    <StudentLabel />
    <div id="admin-scroll-box">
      <StudentDeleteItem
        v-for="(student, index) in students"
        :key="student.id"
        :index="index"
        :student="student"
        @change-check="changeCheck"
      />
    </div>
  </div>
</template>

<script>
import StudentLabel from './StudentLabel.vue'
import StudentDeleteItem from './StudentDeleteItem.vue'
import TheButton from '../common/TheButton.vue'

import axiosAuth from '@/axios/axios'

export default {
  name: 'StudentDelete',
  components: {
    StudentLabel,
    StudentDeleteItem,
    TheButton,
  },
  data() {
    return {
      selected: [],
    }
  },
  computed: {
    axios_URL() {
      return this.$store.state.axios_URL
    },
    access() {
      return this.$store.state.access
    },
    students() {
      return this.$store.state.students
    },
    query() {
      return this.$store.state.query
    },
  },
  methods: {
    changeCheck(value, index) {
      if (value) {
        this.selected.push(index)
      } else {
        for (let i = 0; i < this.selected.length; i++) {
          if (this.selected[i] === index) {
            this.selected.splice(i, 1)
            break
          }
        }
      }
    },
    deleteStudent() {
      if (
        !confirm('정말 삭제하시겠습니까? 해당 학생의 모든 정보가 사라집니다.')
      )
        return

      let delete_list = []
      for (const index of this.selected) {
        delete_list.push(this.students[index].id)
      }
      axiosAuth({
        method: 'delete',
        url: `${this.axios_URL}/students/`,
        headers: {
          Authorization: `Bearer ${this.access}`,
        },
        data: delete_list,
      })
        .then(() => {
          let url
          if (this.$route.query.name)
            url = `students/${this.$route.query.name}/`
          else
            url = `students/${this.$route.query.grade}/${this.$route.query.room}/`

          this.$store.dispatch('getStudents', url)
          this.$router.push({ name: 'student', query: this.query })
        })
        .catch((err) => {
          console.error(err)
          alert('새로고침 후 다시 시도해주세요')
        })
    },
  },
}
</script>

<style></style>
