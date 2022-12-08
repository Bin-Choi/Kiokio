<template>
  <div
    class="d-flex flex-column align-items-center"
    style="width: 100vw; height: 100vh; padding: 7vh">
    <div class="d-flex justify-content-between w-100">
      <div @click="$router.push({ name: 'index' })" style="cursor: pointer">
        <font-awesome-icon icon="fa-solid fa-house" />
        <span>키오스크 홈</span>
      </div>
      <div @click="$store.dispatch('logout')" style="cursor: pointer">
        <font-awesome-icon icon="fa-solid fa-user" />
        <span>로그아웃</span>
      </div>
    </div>

    <div
      class="bg-secondary rounded shadow d-flex flex-column"
      style="width: 100%; height: 80vh; padding: 3vh; margin-top: 5vh">
      <div class="d-flex justify-content-">
        <div class="student-add-btn" @click="createStudent">저장</div>
      </div>
      <div v-if="agGrid">
        <ag-grid-vue
          style="width: 80vw; height: 70vh"
          class="ag-theme-alpine"
          :columnDefs="columnDefs"
          :rowData="rowData"
          rowSelection="multiple"
          @grid-ready="onGridReady">
        </ag-grid-vue>
      </div>
      <div v-if="!agGrid">
        <StudentCreateItem
          v-for="(student, index) in students"
          :key="index"
          :index="index"
          :student="student"
          @change-name="changeName"
          @change-grade="changeGrade"
          @change-room="changeRoom"
          @change-number="changeNumber" />
      </div>
    </div>
  </div>
</template>

<script>
import StudentCreateItem from '@/components/StudentCreateItem.vue'
import { AgGridVue } from 'ag-grid-vue'

export default {
  name: 'StudentCreateView',
  data() {
    return {
      columnDefs: null,
      rowData: null,
      gridApi: null,
      agGrid: true,

      students: [
        { name: null, grade: null, room: null, number: null },
        { name: null, grade: null, room: null, number: null },
        { name: null, grade: null, room: null, number: null },
      ],
    }
  },
  components: {
    StudentCreateItem,
    AgGridVue,
  },
  beforeMount() {
    this.columnDefs = [
      // { field: 'make', sortable: true, filter: true, checkboxSelection: true },
      { field: '이름', sortable: true, filter: true, editable: true },
      { field: '학년', sortable: true, filter: true, editable: true },
      { field: '반', sortable: true, filter: true, editable: true },
      { field: '번호', sortable: true, filter: true, editable: true },
      { field: '성별', sortable: true, filter: true, editable: true },
    ]

    this.rowData = [
      { make: 'Toyota', model: 'Celica', price: 35000 },
      { make: 'Ford', model: 'Mondeo', price: 32000 },
      { make: 'Porsche', model: 'Boxster', price: 72000 },
    ]
  },
  methods: {
    onGridReady(params) {
      this.gridApi = params.api
      this.gridApi.sizeColumnsToFit()
    },
    createStudent() {
      // console.log(this.gridApi.getRowNode(1))
      console.log(this.students)
    },
    changeName(value, index) {
      this.students[index].name = value
    },
    changeGrade(value, index) {
      this.students[index].grade = value
    },
    changeRoom(value, index) {
      this.students[index].room = value
    },
    changeNumber(value, index) {
      this.students[index].number = value
    },
  },
}
</script>

<style scoped>
.student-add-btn {
  background-color: rgb(109, 163, 28);
  width: 10vw;
  height: 5vh;
  border-radius: 1vh;

  color: white;
  line-height: 5vh;
  font-size: 2vh;
  font-weight: bold;
}
</style>
