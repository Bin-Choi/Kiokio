<template>
  <div class="d-flex">
    <div class="col-1 box border">
      {{ index + 1 }}
    </div>
    <div class="col-2 box border">
      {{ student.name }}
    </div>
    <div class="col-1 box border">
      {{ student.grade }}
    </div>
    <div class="col-2 box border">
      {{ student.room }}
    </div>
    <div class="col-2 box border">
      {{ student.number }}
    </div>
    <div class="col-2 box border">
      {{ student.gender }}
    </div>
    <div class="col-2 box border">
      {{ student.password }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'StudentReadItem',
  props: {
    student: Object,
    index: Number,
  },
}
</script>

<style scoped>
.box {
  background-color: white;
}
</style>
