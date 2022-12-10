<template>
  <div class="d-flex">
    <div class="box border">
      {{ index + 1 }}
    </div>
    <div class="clickable-box border" @click="changeModeStudent">
      {{ student.name }}, {{ student.grade }} 학년 {{ student.room }}반
      {{ student.number }} 번
    </div>
    <div
      v-for="(inbody, inbodyIndex) in student.inbody_set"
      :key="inbody.id"
      :inbody-index="inbodyIndex"
      class="clickable-box border"
      @click="changeModeDetail(inbodyIndex)">
      {{ inbody.test_date }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'AdminInbodyItem',
  props: {
    student: Object,
    index: Number,
  },
  methods: {
    changeModeStudent() {
      const studentIndex = this.index
      this.$emit('change-mode-student', studentIndex)
    },
    changeModeDetail(inbodyIndex) {
      const studentIndex = this.index
      this.$emit('change-mode-detail', studentIndex, inbodyIndex)
    },
  },
}
</script>

<style scoped>
.box {
  background-color: white;
}

.clickable-box {
  background-color: white;
  cursor: pointer;
  transition: transform 0.2s linear;
}
.clickable-box:hover {
  background-color: aliceblue;
  transform: scale(1.1);
}
</style>
