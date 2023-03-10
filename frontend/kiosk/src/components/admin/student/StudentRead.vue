<template>
  <div>
    <div class="d-flex justify-content-between">
      <div class="d-flex">
        <TheInput
          :label="'학년'"
          :type="'number'"
          :min="1"
          :refer="'grade'"
          :value="grade"
          :display="'right'"
          @change="
            (v) => {
              this.grade = v
            }
          "
        />
        <TheInput
          :label="'반'"
          :type="'number'"
          :min="1"
          :refer="'room'"
          :value="room"
          :submit="searchByClass"
          :display="'right'"
          @change="
            (v) => {
              this.room = v
            }
          "
        />
        <TheButton :text="'학급 조회'" :onClick="searchByClass" />
      </div>

      <div class="d-flex">
        <TheInput
          :label="'이름'"
          :refer="'name'"
          :value="name"
          :submit="searchByName"
          @change="
            (v) => {
              this.name = v
            }
          "
        />
        <TheButton :text="'이름 조회'" :onClick="searchByName" />
      </div>
    </div>

    <div class="buttons">
      <TheButton
        :color="'green'"
        :text="'등록'"
        :onClick="() => $router.push({ name: 'studentCreate' })"
      />
      <TheButton
        :text="'수정'"
        :onClick="() => $router.push({ name: 'studentUpdate', query })"
      />
      <TheButton
        :color="'red'"
        :text="'삭제'"
        :onClick="() => $router.push({ name: 'studentDelete', query })"
      />
    </div>
    <table>
      <StudentLabel />
      <div id="admin-scroll-box">
        <StudentReadItem
          v-for="(student, index) in students"
          :key="student.id"
          :index="index"
          :student="student"
        />
      </div>
    </table>
  </div>
</template>

<script>
import TheButton from '@/components/admin/common/TheButton.vue'
import TheInput from '@/components/admin/common/TheInput.vue'
import StudentLabel from './StudentLabel.vue'
import StudentReadItem from '@/components/admin/student/StudentReadItem.vue'

export default {
  name: 'StudentRead',
  components: {
    TheButton,
    TheInput,
    StudentLabel,
    StudentReadItem,
  },
  data() {
    return {
      grade: null,
      room: null,
      name: null,
    }
  },
  computed: {
    students() {
      return this.$store.state.students
    },
    query() {
      return this.$store.state.query
    },
  },
  methods: {
    searchByClass() {
      this.$store.commit('SAVE_QUERY', {
        grade: this.grade,
        room: this.room,
        name: this.name,
      })
      this.$router.push({ name: 'student', query: this.query })

      if (!this.grade || !this.room) {
        alert('학년, 반을 모두 입력해주세요')
        return
      }
      //학년 검사
      const regGrade = /^[1-9]$/
      if (!regGrade.test(this.grade)) {
        alert('학년은 1~9사이의 숫자로 입력하세요')
        return
      }
      //반 검사
      const regRoom = /^[1-9]$|^[1-9]{1}[0-9]{1}$/
      if (!regRoom.test(this.room)) {
        alert('반은 1~99사이의 숫자로 입력하세요')
        return
      }
      this.name = null
      const url = `students/${this.grade}/${this.room}/`
      this.$store.dispatch('getStudents', url)
    },
    searchByName() {
      this.$store.commit('SAVE_QUERY', {
        grade: this.grade,
        room: this.room,
        name: this.name,
      })

      this.$router.push({ name: 'student', query: this.query })

      if (!this.name) {
        alert('이름을 입력해주세요')
        return
      }
      const regName = /^[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]{2,}$/
      if (!regName.test(this.name)) {
        alert('이름은 한글 2글자 이상 입력하세요')
        return
      }
      this.grade = null
      this.room = null
      const url = `students/${this.name}/`
      this.$store.dispatch('getStudents', url)
    },
  },
}
</script>

<style>
.buttons {
  display: flex;
  justify-content: flex-end;
  margin: 0.5vh 0;
}

.buttons > button {
  margin-left: 0.5vh;
}
</style>
