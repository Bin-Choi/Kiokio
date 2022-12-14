<template>
  <div class="d-flex" :class="{ 'red-box': invalid === index }">
    <div class="col-1 border box">
      <input
        v-if="readyDelete"
        type="checkbox"
        @change="
          (event) => $emit('change-check', event.target.checked, index)
        " />
      <div v-if="!readyDelete">
        {{ index + 1 }}
      </div>
    </div>
    <input
      type="text"
      :value="student.name"
      maxlength="15"
      class="col-2 border"
      :id="`student-${index * 6}`"
      @keydown.enter="moveOne"
      @keydown.right="moveOne"
      @keydown.left="moveMinusOne"
      @keydown.up="moveMinusSix"
      @keydown.down="moveSix"
      @input="
        (event) => $emit('change-data', event.target.value, index, 'name')
      " />
    <input
      type="number"
      :value="student.grade"
      min="1"
      max="9"
      class="col-1 border"
      :id="`student-${index * 6 + 1}`"
      @keydown.enter="moveOne"
      @keydown.right="moveOne"
      @keydown.left="moveMinusOne"
      @keydown.up="moveMinusSix"
      @keydown.down="moveSix"
      @input="
        (event) => $emit('change-data', event.target.value, index, 'grade')
      " />
    <input
      type="number"
      :value="student.room"
      min="1"
      max="99"
      class="col-2 border"
      :id="`student-${index * 6 + 2}`"
      @keydown.enter="moveOne"
      @keydown.right="moveOne"
      @keydown.left="moveMinusOne"
      @keydown.up="moveMinusSix"
      @keydown.down="moveSix"
      @input="
        (event) => $emit('change-data', event.target.value, index, 'room')
      " />
    <input
      type="number"
      :value="student.number"
      min="0"
      max="99"
      class="col-2 border"
      :id="`student-${index * 6 + 3}`"
      @keydown.enter="moveOne"
      @keydown.right="moveOne"
      @keydown.left="moveMinusOne"
      @keydown.up="moveMinusSix"
      @keydown.down="moveSix"
      @input="
        (event) => $emit('change-data', event.target.value, index, 'number')
      " />
    <select
      name="gender"
      :value="student.gender"
      class="col-2 border"
      :id="`student-${index * 6 + 4}`"
      @keydown.right="moveOne"
      @keydown.left="moveMinusOne"
      @keydown.up="moveMinusSix"
      @keydown.down="moveSix"
      @change="
        (event) => $emit('change-data', event.target.value, index, 'gender')
      ">
      <option :value="null">--선택--</option>
      <option value="남성">남성</option>
      <option value="여성">여성</option>
    </select>
    <input
      type="text"
      :value="student.password"
      maxlength="4"
      class="col-2 border"
      :id="`student-${index * 6 + 5}`"
      @keydown.enter="moveOne"
      @keydown.right="moveOne"
      @keydown.left="moveMinusOne"
      @keydown.up="moveMinusSix"
      @keydown.down="moveSix"
      @input="
        (event) => $emit('change-data', event.target.value, index, 'password')
      " />
  </div>
</template>

<script>
export default {
  name: 'StudentCreateItem',
  props: {
    student: Object,
    index: Number,
    readyDelete: Boolean,
    invalid: Number,
  },
  methods: {
    moveOne(event) {
      event.preventDefault()
      document
        .getElementById(`student-${parseInt(event.target.id.slice(8)) + 1}`)
        .focus()
    },
    moveSix(event) {
      event.preventDefault()
      document
        .getElementById(`student-${parseInt(event.target.id.slice(8)) + 6}`)
        .focus()
    },
    moveMinusOne(event) {
      event.preventDefault()
      document
        .getElementById(`student-${parseInt(event.target.id.slice(8)) - 1}`)
        .focus()
    },
    moveMinusSix(event) {
      event.preventDefault()
      document
        .getElementById(`student-${parseInt(event.target.id.slice(8)) - 6}`)
        .focus()
    },
  },
}
</script>

<style scoped>
.box {
  background-color: white;
}
.red-box {
  outline: 2px solid red;
}
.border:focus {
  background-color: aliceblue;
}
</style>
