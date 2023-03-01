<template>
  <div style="margin-bottom: 1vh">
    <div
      class="d-flex justify-content-between"
      style="margin: 0 0 2vh 0; font-size: 3vh"
    >
      <IconButton
        :icon="'fa-solid fa-circle-arrow-left'"
        :onClick="() => $router.push({ name: 'admin' })"
      />

      <div>출결 관리</div>

      <IconButton
        :class="{ hidden: !students }"
        :icon="'fa-solid fa-table'"
        :text="'다운로드'"
        :onClick="() => $emit('download-excel')"
      />
    </div>

    <div class="d-flex justify-content-start" style="margin-bottom: 1vh">
      <span> ※ 필수 입력값입니다.</span>
    </div>

    <div class="d-flex justify-content-between">
      <div class="d-flex">
        <TheInput
          :label="'년'"
          :type="'number'"
          :min="2000"
          :refer="'year'"
          :display="'right'"
          @change="
            (v) => {
              this.year = v
            }
          "
        />
        <TheInput
          :label="'월'"
          :type="'number'"
          :min="1"
          :max="12"
          :refer="'month'"
          :display="'right'"
          @change="
            (v) => {
              this.month = v
            }
          "
        />
      </div>

      <div class="d-flex">
        <!-- <span>학년</span>
          <input
            type="number"
            min="1"
            class="student-search-form"
            ref="grade"
            v-model.trim="grade"
            @keyup.enter="$refs.room.focus()"
          /> -->

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
      </div>
    </div>
  </div>
</template>

<script>
import TheButton from '@/components/admin/common/TheButton.vue'
import TheInput from '@/components/admin/common/TheInput.vue'
import IconButton from '@/components/admin/common/IconButton.vue'

export default {
  name: 'AttendanceHeader',
  components: {
    TheButton,
    TheInput,
    IconButton,
  },
  props: {
    students: Array,
  },
  data() {
    return {
      year: null,
      month: null,
      grade: null,
      room: null,
      name: null,
    }
  },
  methods: {
    searchByClass() {
      if (!this.year || !this.month) {
        alert('년, 월을 모두 입력해주세요')
      }
      // 년 검사
      const regYear = /^\d{4}$/
      if (!regYear.test(this.year)) {
        alert('년도를 4개의 숫자로 입력해주세요')
        return
      }
      // 월 검사
      const regMonth = /^[1-9]$|^1[012]$/
      if (!regMonth.test(this.month)) {
        alert('월은 1~12의 숫자로 입력해주세요')
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
      this.$emit(
        'search-by-class',
        this.year,
        this.month,
        this.grade,
        this.room
      )
    },
    searchByName() {
      if (!this.year || !this.month) {
        alert('년, 월을 입력하세요')
      }
      // 년 검사
      const regYear = /^\d{4}$/
      if (!regYear.test(this.year)) {
        alert('년도를 4개의 숫자로 입력해주세요')
        return
      }
      // 월 검사
      const regMonth = /^[1-9]$|^1[012]$/
      if (!regMonth.test(this.month)) {
        alert('월은 1~12의 숫자로 입력해주세요')
        return
      }
      if (!this.name) {
        alert('이름을 입력해주세요')
        return
      }

      // 이름 검사
      const regName = /^[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]{2,}$/
      if (!regName.test(this.name)) {
        alert('이름은 한글 2글자 이상 입력하세요')
        return
      }
      this.grade = null
      this.room = null
      this.$emit('search-by-name', this.year, this.month, this.name)
    },
  },
}
</script>

<style scoped>
.hidden {
  visibility: hidden;
}
</style>
