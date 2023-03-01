<template>
  <tr class="d-flex">
    <td class="col-1 box border">
      {{ index + 1 }}
    </td>
    <td class="col-1 box border">
      {{ student.grade }}
    </td>
    <td class="col-2 box border">
      {{ student.room }}
    </td>
    <td class="col-2 box border">
      {{ student.number }}
    </td>
    <td class="col-2 box border">
      {{ student.name }}
    </td>
    <td class="col-2 box border">
      {{ student.gender }}
    </td>
    <td class="col-2 box border">
      {{ student.password }}
    </td>
  </tr>
</template>

<script>
export default {
  name: 'StudentItem',
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
