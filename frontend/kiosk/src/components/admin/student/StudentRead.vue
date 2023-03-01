<template>
  <div>
    <div class="d-flex justify-content-between">
      <div class="d-flex">
        <TheInput
          :label="'학년'"
          :type="'number'"
          :min="1"
          :refer="'grade'"
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
          :submit="searchByName"
          @change="
            (v) => {
              this.name = v
            }
          "
        />
        <TheButton :text="'이름 조회'" :onClick="searchByName" />
        <TheButton
          :color="'green'"
          :text="'+ 학생 등록'"
          :onClick="addStudent"
        />
      </div>
    </div>
    <StudentTableColumn />
    <StudentItem
      v-for="(student, index) in students"
      :key="student.id"
      :index="index"
      :student="student"
    />
  </div>
</template>

<script>
import TheButton from '@/components/admin/common/TheButton.vue'
import TheInput from '../common/TheInput.vue'
import StudentTableColumn from './StudentTableColumn.vue'
import StudentItem from './StudentItem.vue'

export default {
  name: 'StudentRead',
  components: {
    TheButton,
    TheInput,
    StudentTableColumn,
    StudentItem,
  },

  props: {
    students: Array,
  },
  data() {
    return {
      grade: null,
      room: null,
      name: null,
    }
  },
  methods: {
    addStudent() {
      this.$router.push({ name: 'studentCreate' })
    },
    searchByClass() {
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
      this.$emit('search-by-class', this.grade, this.room)
    },
    searchByName() {
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
      this.$emit('search-by-name', this.name)
    },
  },
}
</script>

<style></style>
