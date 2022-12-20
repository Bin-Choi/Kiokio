<template>
  <div class="d-flex flex-column">
    <div class="d-flex justify-content-between">
      <font-awesome-icon
        @click="$emit('change-mode-default')"
        style="font-size: 3vh; cursor: pointer"
        icon="fa-solid fa-circle-arrow-left" />
      <div :class="{ hidden: mode !== 'R' }">
        <font-awesome-icon
          icon="fa-solid fa-table"
          @click="downloadExcel"
          style="font-size: 3vh; cursor: pointer" />
        <div>다운로드</div>
      </div>
    </div>

    <div style="font-size: 2.5vh">
      {{ student.grade }}학년 {{ student.room }}반 {{ student.number }}번
      {{ student.name }} ({{ student.gender }})
    </div>
    <div
      v-if="mode === 'R'"
      class="d-flex justify-content-end"
      style="margin: 1vh 0">
      <button
        class="blue-btn"
        @click="
          inbodyCopy = JSON.parse(JSON.stringify(student.inbody_set))
          mode = 'U'
        ">
        수정
      </button>
    </div>
    <div
      v-if="mode === 'U'"
      class="w-100 d-flex justify-content-between"
      style="margin: 1vh 0">
      <div>
        <button class="gray-btn" @click="mode = 'R'">취소</button>
      </div>
      <div>
        <div v-if="!readyDelete">
          <button class="green-btn" @click="addInbody">기록추가</button>
          <button class="red-btn" @click="deleteInbody">선택삭제</button>
          <button class="blue-btn" @click="updateInbody">저장</button>
        </div>
        <button v-if="readyDelete" class="red-btn" @click="deleteInbody">
          삭제
        </button>
      </div>
    </div>

    <div class="d-flex" id="admin-scroll-box" style="overflow-x: scroll">
      <table class="d-flex" v-if="mode === 'R'" id="inbody-student-table">
        <AdminInbodyStudentTableRow />
        <AdminInbodyStudentReadItem
          v-for="(inbody, index) in student.inbody_set"
          :key="inbody.id"
          :index="index"
          :inbody="inbody" />
      </table>

      <table class="d-flex" v-if="mode === 'U'">
        <AdminInbodyStudentTableRow />
        <AdminInbodyStudentUpdateItem
          v-for="(inbody, index) in inbodyCopy"
          :key="inbody.id"
          :index="index"
          :inbody="inbody"
          :ready-delete="readyDelete"
          :invalid="invalid"
          @change-check="changeCheck"
          @change-data="changeData" />
      </table>
    </div>
  </div>
</template>

<script>
import AdminInbodyStudentTableRow from '@/components/AdminInbodyStudentTableRow.vue'
import AdminInbodyStudentReadItem from '@/components/AdminInbodyStudentReadItem.vue'
import AdminInbodyStudentUpdateItem from '@/components/AdminInbodyStudentUpdateItem.vue'
import * as XLSX from 'xlsx'

import axiosAuth from '@/axios/axios'

export default {
  name: 'AdminInbodyStudent',
  components: {
    AdminInbodyStudentTableRow,
    AdminInbodyStudentReadItem,
    AdminInbodyStudentUpdateItem,
  },
  props: {
    studentIndex: Number,
  },
  data() {
    return {
      mode: 'R',
      inbodyCopy: [],
      readyDelete: false,
      invalid: null,
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
    student() {
      return this.$store.state.inbodyStudents[this.studentIndex]
    },
  },
  methods: {
    addInbody() {
      this.inbodyCopy.push({
        student: this.student.id,
        height: null,
        age: null,
        test_date: null,
        total_body_water: null,
        protein: null,
        minerals: null,
        body_fat_mass: null,
        weight: null,
        skeletal_muscle_mass: null,
        body_mass_index: null,
        percent_body_fat: null,
        inbody_score: null,
      })
    },
    deleteInbody() {
      // 삭제 준비
      if (!this.readyDelete) {
        this.readyDelete = true
        return
      }
      // 삭제 하기
      this.selected.sort(function compare(a, b) {
        // 역순 정렬
        return b - a
      })
      let deleteList = []
      this.selected.forEach((index) => {
        // DB로 보낼 pk 선택
        if (this.inbodyCopy[index].id) {
          deleteList.push(this.inbodyCopy[index].id)
        }
        // 프론트 단에서 삭제
        this.inbodyCopy.splice(index, 1)
      })
      // DB로 삭제 요청
      axiosAuth({
        method: 'delete',
        url: `${this.axios_URL}/students/inbody/list/admin/`,
        headers: {
          Authorization: `Bearer ${this.access}`,
        },
        data: deleteList,
      })
        .then(() => {
          this.selected = []
          this.readyDelete = false
        })
        .catch((err) => {
          console.error(err)
        })
    },
    changeData(value, index, key) {
      this.inbodyCopy[index][key] = value
    },
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
    updateInbody() {
      //유효성 검사
      this.invalid = null
      const inbodyCopy = this.inbodyCopy

      const regDate = /^\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$/

      const regFloatBlank = /(^\d*$)|(^\d{1,}.\d{1,2}$)/
      const regFloat = /(^\d+$)|(^\d{1,}.\d{1,2}$)/
      const regInt = /^[0-9]+$/
      for (let i = 0; i < inbodyCopy.length; i++) {
        //날짜 검사
        if (!regDate.test(inbodyCopy[i].test_date)) {
          this.invalid = i
          alert('날짜를 선택해주세요')
          return
        }
        //키 검사
        if (!regFloat.test(inbodyCopy[i].height)) {
          this.invalid = i
          alert('키는 소수점 둘째자리까지 입력가능합니다.')
          return
        }
        //나이 검사
        if (!regInt.test(inbodyCopy[i].age)) {
          this.invalid = i
          alert('나이는 정수로 입력가능합니다.')
          return
        }
        //체중
        if (!regFloat.test(inbodyCopy[i].weight)) {
          this.invalid = i
          alert('체중은 소수점 둘째자리까지 입력가능합니다.')
          return
        }
        //BMI
        if (!regFloat.test(inbodyCopy[i].body_mass_index)) {
          this.invalid = i
          alert('BMI는 소수점 둘째자리까지 입력가능합니다.')
          return
        }
        //체지방률
        if (!regFloat.test(inbodyCopy[i].percent_body_fat)) {
          this.invalid = i
          alert('체지방률은 소수점 둘째자리까지 입력가능합니다.')
          return
        }
        //체수분
        if (
          inbodyCopy[i].total_body_water &&
          !regFloatBlank.test(inbodyCopy[i].total_body_water)
        ) {
          this.invalid = i
          alert('체수분은 소수점 둘째자리까지 입력가능합니다.')
          return
        }
        //단백질
        if (
          inbodyCopy[i].protein &&
          !regFloatBlank.test(inbodyCopy[i].protein)
        ) {
          this.invalid = i
          alert('단백질은 소수점 둘째자리까지 입력가능합니다.')
          return
        }
        //무기질
        if (
          inbodyCopy[i].minerals &&
          !regFloatBlank.test(inbodyCopy[i].minerals)
        ) {
          this.invalid = i
          alert('미네랄은 소수점 둘째자리까지 입력가능합니다.')
          return
        }
        //체지방량
        if (
          inbodyCopy[i].total_fat_mass &&
          !regFloatBlank.test(inbodyCopy[i].body_fat_mass)
        ) {
          this.invalid = i
          alert('체지방량은 소수점 둘째자리까지 입력가능합니다.')
          return
        }
        //골격근량
        if (
          inbodyCopy[i].skeletal_muscle_mass &&
          !regFloatBlank.test(inbodyCopy[i].skeletal_muscle_mass)
        ) {
          this.invalid = i
          alert('골격근량은 소수점 둘째자리까지 입력가능합니다.')
          return
        }
        //인바디 점수
        if (
          inbodyCopy[i].inbody_score &&
          !regFloatBlank.test(inbodyCopy[i].inbody_score)
        ) {
          this.invalid = i
          alert('인바디 점수는 소수점 둘째자리까지 입력가능합니다.')
          return
        }
      }
      axiosAuth({
        method: 'put',
        url: `${this.axios_URL}/students/inbody/list/admin/`,
        headers: {
          Authorization: `Bearer ${this.access}`,
        },
        data: this.inbodyCopy,
      })
        .then((res) => {
          console.log(res)
          const payload = {
            studentIndex: this.studentIndex,
            inbodyList: res.data,
          }
          this.$store.commit('CHANGE_STUDENT_INBODY', payload)
          this.mode = 'R'
          this.inbodyCopy = []
        })
        .catch((err) => {
          console.error(err)
        })
    },
    downloadExcel() {
      const excelData = XLSX.utils.table_to_sheet(
        document.getElementById('inbody-student-table')
      ) // table id를 넣어주면된다
      const workBook = XLSX.utils.book_new() // 새 시트 생성
      XLSX.utils.book_append_sheet(workBook, excelData, '인바디내역') // 시트 명명, 데이터 지정
      XLSX.writeFile(
        workBook,
        `${this.student.grade}학년_${this.student.room}반_${this.student.number}번_${this.student.name}_인바디내역.xlsx`
      ) // 엑셀파일 만듬
    },
  },
}
</script>

<style scoped>
button {
  margin-left: 1vh;
}
.hidden {
  visibility: hidden;
}
</style>
