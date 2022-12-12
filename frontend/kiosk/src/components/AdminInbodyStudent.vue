<template>
  <div class="d-flex flex-column">
    <div
      class="d-flex"
      @click="$emit('change-mode-default')"
      style="font-size: 4vh; cursor: pointer"
    >
      <font-awesome-icon icon="fa-solid fa-circle-arrow-left" />
    </div>

    <div>
      {{ student.name }} {{ student.grade }}학년 {{ student.room }}반
      {{ student.number }}번호 {{ student.gender }}
    </div>
    <div
      v-if="mode === 'R'"
      class="d-flex justify-content-end"
      style="margin: 1vh 0"
    >
      <button
        class="blue-btn"
        @click="
          inbodyCopy = JSON.parse(JSON.stringify(student.inbody_set))
          mode = 'U'
        "
      >
        수정
      </button>
    </div>
    <div v-if="mode === 'U'">
      <button class="gray-btn" @click="mode = 'R'">취소</button>
      <button class="green-btn" @click="addInbody">추가</button>
      <button class="red-btn" @click="deleteInbody">삭제</button>
      <button class="blue-btn" @click="updateInbody">저장</button>
    </div>

    <div class="d-flex" style="overflow-x: scroll">
      <AdminInbodyStudentTableRow />

      <div class="d-flex" v-if="mode === 'R'">
        <AdminInbodyStudentReadItem
          v-for="(inbody, index) in student.inbody_set"
          :key="inbody.id"
          :index="index"
          :inbody="inbody"
        />
      </div>

      <div class="d-flex" v-if="mode === 'U'">
        <AdminInbodyStudentUpdateItem
          v-for="(inbody, index) in inbodyCopy"
          :key="inbody.id"
          :index="index"
          :inbody="inbody"
          :ready-delete="readyDelete"
          :invalid="invalid"
          @change-check="changeCheck"
          @change-data="changeData"
        />
      </div>
    </div>
  </div>
</template>

<script>
import AdminInbodyStudentTableRow from '@/components/AdminInbodyStudentTableRow.vue'
import AdminInbodyStudentReadItem from '@/components/AdminInbodyStudentReadItem.vue'
import AdminInbodyStudentUpdateItem from '@/components/AdminInbodyStudentUpdateItem.vue'

import axios from 'axios'

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
      if (!this.readyDelete) {
        this.readyDelete = true
      } else {
        this.selected.sort(function compare(a, b) {
          return b - a
        })
        this.selected.forEach((index) => {
          this.inbodyCopy.splice(index, 1)
        })
        this.selected = []
        this.readyDelete = false
      }
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
      for (let i = 0; i < inbodyCopy.length; i++) {
        const regDate = /^\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$/
        const regInt = /^\d+$/
        const regFloat = /^\d+[.]\d{1}$/
        //날짜 검사
        if (!regDate.test(inbodyCopy[i].test_date)) {
          this.invalid = i
          alert('날짜를 선택해주세요')
          return
        }
        //키 검사
        if (!regInt.test(inbodyCopy[i].height)) {
          this.invalid = i
          alert('키를 정수로 입력하세요')
          return
        }
        //나이 검사
        if (!regInt.test(inbodyCopy[i].age)) {
          this.invalid = i
          alert('나이를 정수로 입력하세요')
          return
        }
        //체수분
        if (!regFloat.test(inbodyCopy[i].total_body_water)) {
          this.invalid = i
          alert('체수분을 소수로 입력하세요')
          return
        }
        //단백질
        if (!regFloat.test(inbodyCopy[i].protein)) {
          this.invalid = i
          alert('단백질을 소수로 입력하세요')
          return
        }
        //무기질
        if (!regFloat.test(inbodyCopy[i].minerals)) {
          this.invalid = i
          alert('미네랄을 소수로 입력하세요')
          return
        }
        //체지방량
        if (!regFloat.test(inbodyCopy[i].body_fat_mass)) {
          this.invalid = i
          alert('체지방량을 소수로 입력하세요')
          return
        }
        //체중
        if (!regFloat.test(inbodyCopy[i].weight)) {
          this.invalid = i
          alert('체중을 소수로 입력하세요')
          return
        }
        //골격근량
        if (!regFloat.test(inbodyCopy[i].skeletal_muscle_mass)) {
          this.invalid = i
          alert('골격근량을 소수로 입력하세요')
          return
        }
        //BMI
        if (!regFloat.test(inbodyCopy[i].body_mass_index)) {
          this.invalid = i
          alert('BMI를 소수로 입력하세요')
          return
        }
        //체지방률
        if (!regFloat.test(inbodyCopy[i].percent_body_fat)) {
          this.invalid = i
          alert('체지방률을 소수로 입력하세요')
          return
        }
        //인바디 점수
        if (!regInt.test(inbodyCopy[i].inbody_score)) {
          this.invalid = i
          alert('인바디 점수를 정수로 입력하세요')
          return
        }
      }
      axios({
        method: 'post',
        url: `${this.axios_URL}/students/inbody/update/admin/`,
        headers: {
          Authorization: `Bearer ${this.access}`,
        },
        data: this.inbodyCopy,
      })
        .then((res) => {
          console.log(res)
          console.log(this.inbodyCopy)
          const payload = {
            studentIndex: this.studentIndex,
            inbodyList: this.inbodyCopy,
          }
          this.$store.commit('CHANGE_STUDENT_INBODY', payload)
          this.mode = 'R'
        })
        .catch((err) => {
          console.error(err)
        })
    },
  },
}
</script>

<style scoped></style>
