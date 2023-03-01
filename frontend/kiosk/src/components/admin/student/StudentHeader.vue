<template>
  <div class="d-flex flex-column" style="margin-bottom: 1vh; min-width: 550px">
    <div
      class="d-flex justify-content-between"
      style="margin: 0 0 2vh 0; font-size: 3vh"
    >
      <font-awesome-icon
        icon="fa-solid fa-circle-arrow-left"
        @click="$router.push({ name: 'admin' })"
        style="cursor: pointer"
      />
      <div>학생 관리</div>
      <div :class="{ hidden: !students }">
        <font-awesome-icon
          icon="fa-solid fa-table"
          @click="$emit('download-excel')"
          style="cursor: pointer"
        />
        <div style="font-size: 1.5vh">다운로드</div>
      </div>
    </div>

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
  </div>
</template>

<script>
import TheButton from '@/components/admin/common/TheButton.vue'
import TheInput from '@/components/admin/common/TheInput.vue'

export default {
  name: 'StudentHeader',
  components: {
    TheButton,
    TheInput,
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

<style scoped>
.hidden {
  visibility: hidden;
}
</style>
