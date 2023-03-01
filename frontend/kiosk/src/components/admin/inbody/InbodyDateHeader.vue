<template>
  <div class="d-flex flex-column" style="margin-bottom: 1vh; min-width: 710px">
    <div
      class="d-flex justify-content-between"
      style="margin: 0 0 2vh 0; font-size: 3vh"
    >
      <IconButton
        :icon="'fa-solid fa-circle-arrow-left'"
        :onClick="() => $router.push({ name: 'admin' })"
      />

      <div>인바디 관리</div>

      <IconButton
        :class="{ hidden: mode !== 'R' || !inbodies }"
        :icon="'fa-solid fa-table'"
        :text="'다운로드'"
        :onClick="() => $emit('download-excel')"
      />
    </div>

    <div class="d-flex justify-content-between">
      <TheInput
        :type="'date'"
        :refer="'date'"
        :display="'long'"
        @change="(v) => (this.date = v)"
      />
      <div class="d-flex">
        <TheInput
          :label="'학년'"
          :type="'number'"
          :min="1"
          :refer="'grade'"
          :display="'right'"
          @change="(v) => (this.grade = v)"
        />
        <TheInput
          :label="'반'"
          :type="'number'"
          :min="1"
          :refer="'room'"
          :submit="searchByClass"
          :display="'right'"
          @change="(v) => (this.room = v)"
        />
        <TheButton :text="'학급 조회'" :onClick="searchByClass" />

        <TheInput
          :label="'이름'"
          :refer="'name'"
          :submit="searchByName"
          @change="(v) => (this.name = v)"
        />
        <TheButton :text="'이름 조회'" :onClick="searchByName" />
      </div>
    </div>
  </div>
</template>

<script>
import TheButton from '@/components/admin/common/TheButton.vue'
import TheInput from '@/components/admin/common/TheInput.vue'
import IconButton from '@/components/admin/common/IconButton.vue'

export default {
  name: 'InbodyDateHeader',
  components: {
    TheButton,
    TheInput,
    IconButton,
  },
  props: {
    inbodies: Array,
    mode: String,
  },
  data() {
    return {
      date: null,
      grade: null,
      room: null,
      name: null,
    }
  },
  methods: {
    searchByClass() {
      const regDate = /^\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$/
      if (!regDate.test(this.date)) {
        alert('날짜를 선택해주세요')
        return
      }
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
      this.$emit('search-by-class', this.date, this.grade, this.room)
    },
    searchByName() {
      const regDate = /^\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$/
      if (!regDate.test(this.date)) {
        alert('날짜를 선택해주세요')
        return
      }
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
      this.$emit('search-by-name', this.date, this.name)
    },
  },
}
</script>

<style scoped>
.hidden {
  visibility: hidden;
}
</style>
