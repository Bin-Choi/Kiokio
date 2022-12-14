<template>
  <div class="d-flex flex-column" :class="{ 'red-box': invalid === index }">
    <div class="box border">
      <input
        v-if="readyDelete"
        type="checkbox"
        @change="(event) => $emit('change-check', event.target.checked, index)"
      />
      <div v-if="!readyDelete">
        {{ index + 1 }}
      </div>
    </div>
    <input
      type="date"
      :value="inbody.test_date"
      class="box border"
      :id="`inbody-${index * 12}`"
      @keydown.enter="moveOne"
      @keydown.right="moveTwelve"
      @keydown.left="moveMinusTwelve"
      @keydown.up="moveMinusOne"
      @keydown.down="moveOne"
      @input="
        (event) => $emit('change-data', event.target.value, index, 'test_date')
      "
    />
    <input
      type="number"
      :value="inbody.height"
      step="0.1"
      class="box border"
      :id="`inbody-${index * 12 + 1}`"
      @keydown.enter="moveOne"
      @keydown.right="moveTwelve"
      @keydown.left="moveMinusTwelve"
      @keydown.up="moveMinusOne"
      @keydown.down="moveOne"
      @input="
        (event) => $emit('change-data', event.target.value, index, 'height')
      "
    />
    <input
      type="number"
      :value="inbody.age"
      class="box border"
      :id="`inbody-${index * 12 + 2}`"
      @keydown.enter="moveOne"
      @keydown.right="moveTwelve"
      @keydown.left="moveMinusTwelve"
      @keydown.up="moveMinusOne"
      @keydown.down="moveOne"
      @input="(event) => $emit('change-data', event.target.value, index, 'age')"
    />
    <input
      type="number"
      :value="inbody.weight"
      step="0.1"
      class="box border"
      :id="`inbody-${index * 12 + 3}`"
      @keydown.enter="moveOne"
      @keydown.right="moveTwelve"
      @keydown.left="moveMinusTwelve"
      @keydown.up="moveMinusOne"
      @keydown.down="moveOne"
      @input="
        (event) => $emit('change-data', event.target.value, index, 'weight')
      "
    />
    <input
      type="number"
      :value="inbody.body_mass_index"
      step="0.1"
      class="box border"
      :id="`inbody-${index * 12 + 4}`"
      @keydown.enter="moveOne"
      @keydown.right="moveTwelve"
      @keydown.left="moveMinusTwelve"
      @keydown.up="moveMinusOne"
      @keydown.down="moveOne"
      @input="
        (event) =>
          $emit('change-data', event.target.value, index, 'body_mass_index')
      "
    />
    <input
      type="number"
      :value="inbody.percent_body_fat"
      step="0.1"
      class="box border"
      :id="`inbody-${index * 12 + 5}`"
      @keydown.enter="moveOne"
      @keydown.right="moveTwelve"
      @keydown.left="moveMinusTwelve"
      @keydown.up="moveMinusOne"
      @keydown.down="moveOne"
      @input="
        (event) =>
          $emit('change-data', event.target.value, index, 'percent_body_fat')
      "
    />
    <input
      type="number"
      :value="inbody.total_body_water"
      step="0.1"
      class="box border"
      :id="`inbody-${index * 12 + 6}`"
      @keydown.enter="moveOne"
      @keydown.right="moveTwelve"
      @keydown.left="moveMinusTwelve"
      @keydown.up="moveMinusOne"
      @keydown.down="moveOne"
      @input="
        (event) =>
          $emit('change-data', event.target.value, index, 'total_body_water')
      "
    />
    <input
      type="number"
      :value="inbody.protein"
      step="0.1"
      class="box border"
      :id="`inbody-${index * 12 + 7}`"
      @keydown.enter="moveOne"
      @keydown.right="moveTwelve"
      @keydown.left="moveMinusTwelve"
      @keydown.up="moveMinusOne"
      @keydown.down="moveOne"
      @input="
        (event) => $emit('change-data', event.target.value, index, 'protein')
      "
    />
    <input
      type="number"
      :value="inbody.minerals"
      step="0.1"
      class="box border"
      :id="`inbody-${index * 12 + 8}`"
      @keydown.enter="moveOne"
      @keydown.right="moveTwelve"
      @keydown.left="moveMinusTwelve"
      @keydown.up="moveMinusOne"
      @keydown.down="moveOne"
      @input="
        (event) => $emit('change-data', event.target.value, index, 'minerals')
      "
    />
    <input
      type="number"
      :value="inbody.body_fat_mass"
      step="0.1"
      class="box border"
      :id="`inbody-${index * 12 + 9}`"
      @keydown.enter="moveOne"
      @keydown.right="moveTwelve"
      @keydown.left="moveMinusTwelve"
      @keydown.up="moveMinusOne"
      @keydown.down="moveOne"
      @input="
        (event) =>
          $emit('change-data', event.target.value, index, 'body_fat_mass')
      "
    />
    <input
      type="number"
      :value="inbody.skeletal_muscle_mass"
      step="0.1"
      class="box border"
      :id="`inbody-${index * 12 + 10}`"
      @keydown.enter="moveOne"
      @keydown.right="moveTwelve"
      @keydown.left="moveMinusTwelve"
      @keydown.up="moveMinusOne"
      @keydown.down="moveOne"
      @input="
        (event) =>
          $emit(
            'change-data',
            event.target.value,
            index,
            'skeletal_muscle_mass'
          )
      "
    />
    <input
      type="number"
      :value="inbody.inbody_score"
      step="0.1"
      class="box border"
      :id="`inbody-${index * 12 + 11}`"
      @keydown.enter="moveOne"
      @keydown.right="moveTwelve"
      @keydown.left="moveMinusTwelve"
      @keydown.up="moveMinusOne"
      @keydown.down="moveOne"
      @input="
        (event) =>
          $emit('change-data', event.target.value, index, 'inbody_score')
      "
    />
  </div>
</template>

<script>
export default {
  name: 'AdminInbodyStudentUpdateItem',
  props: {
    inbody: Object,
    index: Number,
    readyDelete: Boolean,
    invalid: Number,
  },
  methods: {
    moveOne(event) {
      event.preventDefault()
      document
        .getElementById(`inbody-${parseInt(event.target.id.slice(7)) + 1}`)
        .focus()
    },
    moveTwelve(event) {
      event.preventDefault()
      document
        .getElementById(`inbody-${parseInt(event.target.id.slice(7)) + 12}`)
        .focus()
    },
    moveMinusOne(event) {
      event.preventDefault()
      document
        .getElementById(`inbody-${parseInt(event.target.id.slice(7)) - 1}`)
        .focus()
    },
    moveMinusTwelve(event) {
      event.preventDefault()
      document
        .getElementById(`inbody-${parseInt(event.target.id.slice(7)) - 12}`)
        .focus()
    },
  },
}
</script>

<style scoped>
.box {
  background-color: white;
  height: 30px;
}
.red-box {
  height: fit-content;
  border: 0.3vh solid red;
}
.border:focus {
  background-color: aliceblue;
}
</style>
