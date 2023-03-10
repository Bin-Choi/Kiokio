<template>
  <div class="item round shadow" @click="clicked">
    <p>{{ this.gym.title }}</p>
    <img :src="imgSrc" alt="gym" style="width: 60%" />
  </div>
</template>

<script>
export default {
  name: 'GymItem',

  props: {
    gym: Object,
  },
  computed: {
    imgSrc() {
      return this.gym.photo
    },
  },
  methods: {
    clicked() {
      this.$emit('show-modal')
      this.$store.commit('GET_GYM_CONTENT', this.gym)
    },
  },
}
</script>

<style scoped>
.item {
  width: 15vh;
  height: 15vh;
  margin: 0.8vh;
  padding: 1vh;
  border: 0.1vh solid #ffa946;
}
</style>
