<template>
  <div class="item round shadow" @click="$emit('show-modal')">
    <img src="#" alt="img" />
    <div>{{ this.gym }}</div>
  </div>
</template>

<script>
export default {
  name: 'GymItem',

  // temporary data
  props: {
    gym: String,
  },
  methods: {},
}
</script>

<style scoped>
.item {
  width: 15vh;
  height: 15vh;
  margin: 0.8vh;
  border: 0.1vh solid #ffa946;
}
</style>
