<template>
  <div
    class="bg-white d-flex flex-column align-items-center"
    style="height: 100vh; padding: 7vh"
  >
    <AdminHeader />

    <div class="inbodyContent rounded shadow d-flex flex-column">
      <AdminInbodyDateHeader
        @search-by-class="searchByClass"
        @search-by-name="searchByName"
        @download-excel="downloadExcel"
        :inbodies="inbodies"
        :mode="mode"
      />

      <div v-if="inbodies">
        <!-- INBODY CONTENT -->
        <div class="button-box" v-if="mode === 'R'">
          <button class="blue-btn shadow-sm" @click="mode = 'U'">수정</button>
          <button
            class="red-btn shadow-sm"
            style="margin-left: 1vh"
            @click="mode = 'D'"
          >
            삭제
          </button>
        </div>
        <div class="button-box" v-if="mode === 'U'">
          <button class="blue-btn shadow-sm" @click="updateInbody">저장</button>
        </div>
        <div class="button-box" v-if="mode === 'D'">
          <button class="red-btn shadow-sm" @click="deleteInbody">삭제</button>
        </div>

        <div id="admin-scroll-box" style="height: 55vh">
          <div v-if="mode === 'R'">
            <table style="margin-bottom: 0.5vh" id="inbody-date-table">
              <AdminInbodyDateTableColumn />
              <AdminInbodyDateReadItem
                v-for="(inbody, index) in inbodies"
                :key="inbody.id"
                :inbody="inbody"
                :index="index"
              />
            </table>
          </div>
          <div v-if="mode === 'U'">
            <table style="margin-bottom: 0.5vh">
              <AdminInbodyDateTableColumn />
              <AdminInbodyDateUpdateItem
                v-for="(inbody, index) in inbodies"
                :key="inbody.id"
                :inbody="inbody"
                :index="index"
                :invalid="invalid"
                @change-data="changeData"
              />
            </table>
          </div>
          <div v-if="mode === 'D'">
            <table style="margin-bottom: 0.5vh">
              <AdminInbodyDateTableColumn />
              <AdminInbodyDateDeleteItem
                v-for="(inbody, index) in inbodies"
                :key="inbody.id"
                :inbody="inbody"
                :index="index"
                @change-check="changeCheck"
              />
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AdminHeader from '@/components/AdminHeader.vue'
import AdminInbodyDateHeader from '@/components/AdminInbodyDateHeader.vue'
import AdminInbodyDateTableColumn from '@/components/AdminInbodyDateTableColumn.vue'
import AdminInbodyDateReadItem from '@/components/AdminInbodyDateReadItem.vue'
import AdminInbodyDateUpdateItem from '@/components/AdminInbodyDateUpdateItem.vue'
import AdminInbodyDateDeleteItem from '@/components/AdminInbodyDateDeleteItem.vue'
import axiosAuth from '@/axios/axios'
import * as XLSX from 'xlsx'

export default {
  name: 'AdminInbodyDateView',
  components: {
    AdminHeader,
    AdminInbodyDateHeader,
    AdminInbodyDateTableColumn,
    AdminInbodyDateReadItem,
    AdminInbodyDateUpdateItem,
    AdminInbodyDateDeleteItem,
  },
  data() {
    return {
      mode: 'R',
      inbodies: null,
      invalid: null,
      selected: [],
      date: null,
      name: null,
      grade: null,
      room: null,
    }
  },
  computed: {
    axios_URL() {
      return this.$store.state.axios_URL
    },
    access() {
      return this.$store.state.access
    },
  },
  methods: {
    // Read
    searchByClass(date, grade, room) {
      this.date = date
      this.grade = grade
      this.room = room
      this.name = null
      const url = `${this.axios_URL}/students/${date}/${grade}/${room}/inbody/admin/date/`
      this.searchStudent(url)
    },
    searchByName(date, name) {
      this.date = date
      this.grade = null
      this.room = null
      this.name = name
      const url = `${this.axios_URL}/students/${date}/${name}/inbody/admin/date/`
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
          this.inbodies = res.data
        })
        .catch((err) => {
          console.error(err)
          alert('해당 정보의 학생이 존재하지 않습니다')
        })
    },
    // Update
    changeData(value, index, key) {
      this.inbodies[index][key] = value
    },
    updateInbody() {
      //유효성 검사
      this.invalid = null
      const inbodies = this.inbodies

      const regDate = /^\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$/
      const regFloatBlank = /(^\d*$)|(^\d{1,}.\d{1,2}$)/
      const regFloat = /(^\d+$)|(^\d{1,}.\d{1,2}$)/
      const regInt = /^[0-9]+$/
      for (let i = 0; i < inbodies.length; i++) {
        //날짜 검사
        if (!regDate.test(inbodies[i].test_date)) {
          this.invalid = i
          alert('날짜를 선택해주세요')
          return
        }
        //키 검사
        if (!regFloat.test(inbodies[i].height)) {
          this.invalid = i
          alert('키는 소수점 둘째자리까지 입력가능합니다.')
          return
        }
        //나이 검사
        if (!regInt.test(inbodies[i].age)) {
          this.invalid = i
          alert('나이는 정수로 입력가능합니다.')
          return
        }
        //체중
        if (!regFloat.test(inbodies[i].weight)) {
          this.invalid = i
          alert('체중은 소수점 둘째자리까지 입력가능합니다.')
          return
        }
        //BMI
        if (!regFloat.test(inbodies[i].body_mass_index)) {
          this.invalid = i
          alert('BMI는 소수점 둘째자리까지 입력가능합니다.')
          return
        }
        //체지방률
        if (!regFloat.test(inbodies[i].percent_body_fat)) {
          this.invalid = i
          alert('체지방률은 소수점 둘째자리까지 입력가능합니다.')
          return
        }
        //체수분
        if (
          inbodies[i].total_body_water &&
          !regFloatBlank.test(inbodies[i].total_body_water)
        ) {
          this.invalid = i
          alert('체수분은 소수점 둘째자리까지 입력가능합니다.')
          return
        }
        //단백질
        if (inbodies[i].protein && !regFloatBlank.test(inbodies[i].protein)) {
          this.invalid = i
          alert('단백질은 소수점 둘째자리까지 입력가능합니다.')
          return
        }
        //무기질
        if (inbodies[i].minerals && !regFloatBlank.test(inbodies[i].minerals)) {
          this.invalid = i
          alert('미네랄은 소수점 둘째자리까지 입력가능합니다.')
          return
        }
        //체지방량
        if (
          inbodies[i].total_fat_mass &&
          !regFloatBlank.test(inbodies[i].body_fat_mass)
        ) {
          this.invalid = i
          alert('체지방량은 소수점 둘째자리까지 입력가능합니다.')
          return
        }
        //골격근량
        if (
          inbodies[i].skeletal_muscle_mass &&
          !regFloatBlank.test(inbodies[i].skeletal_muscle_mass)
        ) {
          this.invalid = i
          alert('골격근량은 소수점 둘째자리까지 입력가능합니다.')
          return
        }
        //인바디 점수
        if (
          inbodies[i].inbody_score &&
          !regFloatBlank.test(inbodies[i].inbody_score)
        ) {
          this.invalid = i
          alert('인바디 점수는 소수점 둘째자리까지 입력가능합니다.')
          return
        }
      }
      axiosAuth({
        method: 'put',
        url: `${this.axios_URL}/students/inbody/list/date/`,
        headers: {
          Authorization: `Bearer ${this.access}`,
        },
        data: this.inbodies,
      })
        .then(() => {
          this.mode = 'R'
        })
        .catch((err) => {
          console.error(err)
          alert('새로고침 후 다시 시도해주세요')
        })
    },
    // Delete
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
    deleteInbody() {
      let delete_list = []
      for (const index of this.selected) {
        delete_list.push(this.inbodies[index].id)
      }
      axiosAuth({
        method: 'delete',
        url: `${this.axios_URL}/students/inbody/list/date/`,
        headers: {
          Authorization: `Bearer ${this.access}`,
        },
        data: delete_list,
      })
        .then((res) => {
          console.log(res)
          this.selected.sort(function compare(a, b) {
            return b - a
          })
          this.selected.forEach((index) => {
            this.inbodies.splice(index, 1)
          })
          this.selected = []
          this.mode = 'R'
        })
        .catch((err) => {
          console.error(err)
          alert('새로고침 후 다시 시도해주세요')
        })
    },
    downloadExcel() {
      let fileName = ''
      if (this.name) {
        fileName = `${this.date}_${this.name}_인바디기록.xlsx`
      } else {
        fileName = `${this.date}_${this.grade}학년_${this.room}반_인바디기록.xlsx`
      }
      const excelData = XLSX.utils.table_to_sheet(
        document.getElementById('inbody-date-table')
      ) // table id를 넣어주면된다
      const workBook = XLSX.utils.book_new() // 새 시트 생성
      XLSX.utils.book_append_sheet(workBook, excelData, '인바디기록') // 시트 명명, 데이터 지정
      XLSX.writeFile(workBook, fileName) // 엑셀파일 만듬
    },
  },
}
</script>

<style scoped>
.inbodyContent {
  width: 100%;
  height: 80vh;
  padding: 3vh;
  margin-top: 3vh;
  background-color: #81a0bb4b;
  min-width: 750px;
}
.button-box {
  margin-bottom: 1vh;
  display: flex;
  justify-content: end;
}
</style>
