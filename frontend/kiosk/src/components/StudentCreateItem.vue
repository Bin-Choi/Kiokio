<template>
  <div class="d-flex">
    <input
      type="text"
      class="col-4 outline"
      @input="(event) => $emit('change-name', event.target.value, index)" />
    <input
      type="number"
      class="col-2 outline"
      @input="(event) => $emit('change-grade', event.target.value, index)" />
    <input
      type="number"
      class="col-2 outline"
      @input="(event) => $emit('change-room', event.target.value, index)" />
    <input
      type="number"
      class="col-2 outline"
      @input="(event) => $emit('change-number', event.target.value, index)" />
  </div>
</template>

<script>
export default {
  name: 'StudentCreateItem',
  props: {
    student: Object,
    index: Number,
  },
}
</script>

<style scoped>
.outline {
  outline: 1px solid black;
}
</style>
