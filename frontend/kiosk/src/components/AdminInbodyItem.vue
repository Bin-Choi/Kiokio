<template>
  <div class="d-flex">
    <div class="box border" style="width: 5vh">
      {{ index + 1 }}
    </div>
    <div class="box border" style="width: 6vh">
      {{ student.grade }}
    </div>
    <div class="box border" style="width: 6vh">
      {{ student.room }}
    </div>
    <div class="box border" style="width: 6vh">
      {{ student.number }}
    </div>
    <div
      class="clickable-box border"
      @click="changeModeStudent"
      style="width: 10vh"
    >
      {{ student.name }}
    </div>
    <div
      v-for="(inbody, inbodyIndex) in student.inbody_set"
      :key="inbody.id"
      :inbody-index="inbodyIndex"
      class="clickable-box border"
      style="padding-left: 1vh; padding-right: 1vh"
      @click="changeModeDetail(inbodyIndex)"
    >
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
