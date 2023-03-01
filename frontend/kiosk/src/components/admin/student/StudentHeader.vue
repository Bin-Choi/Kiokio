<template>
  <div class="d-flex flex-column" style="margin-bottom: 1vh; min-width: 550px">
    <div
      class="d-flex justify-content-between"
      style="margin: 0 0 2vh 0; font-size: 3vh"
    >
      <IconButton
        :icon="'fa-solid fa-circle-arrow-left'"
        :onClick="() => $router.push({ name: 'admin' })"
      />

      <div>학생 관리</div>

      <IconButton
        :class="{ hidden: !students }"
        :icon="'fa-solid fa-table'"
        :text="'다운로드'"
        :onClick="() => $emit('download-excel')"
      />
    </div>
  </div>
</template>

<script>
// import TheButton from '@/components/admin/common/TheButton.vue'
// import TheInput from '@/components/admin/common/TheInput.vue'
import IconButton from '../common/IconButton.vue'
export default {
  name: 'StudentHeader',
  components: {
    // TheButton,
    // TheInput,
    IconButton,
  },
  props: {
    students: Array,
  },
  // data() {
  //   return {
  //     grade: null,
  //     room: null,
  //     name: null,
  //   }
  // },
  // methods: {
  //   addStudent() {
  //     this.$router.push({ name: 'studentCreate' })
  //   },
  //   searchByClass() {
  //     if (!this.grade || !this.room) {
  //       alert('학년, 반을 모두 입력해주세요')
  //       return
  //     }
  //     //학년 검사
  //     const regGrade = /^[1-9]$/
  //     if (!regGrade.test(this.grade)) {
  //       alert('학년은 1~9사이의 숫자로 입력하세요')
  //       return
  //     }
  //     //반 검사
  //     const regRoom = /^[1-9]$|^[1-9]{1}[0-9]{1}$/
  //     if (!regRoom.test(this.room)) {
  //       alert('반은 1~99사이의 숫자로 입력하세요')
  //       return
  //     }
  //     this.name = null
  //     this.$emit('search-by-class', this.grade, this.room)
  //   },
  //   searchByName() {
  //     if (!this.name) {
  //       alert('이름을 입력해주세요')
  //       return
  //     }
  //     const regName = /^[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]{2,}$/
  //     if (!regName.test(this.name)) {
  //       alert('이름은 한글 2글자 이상 입력하세요')
  //       return
  //     }
  //     this.grade = null
  //     this.room = null
  //     this.$emit('search-by-name', this.name)
  //   },
  // },
}
</script>

<style scoped>
.hidden {
  visibility: hidden;
}
</style>
