<template>
  <div class="item rounded shadow" @click="$emit('show-modal')">
      <img src="#" alt="img">
      <div>{{this.gym}}</div>
  </div>
</template>

<script>
export default {
  name: 'GymItem',

  // temporary data
  props:{
    gym:String,
  },
  methods:{
  }
}
</script>

<style scoped>
.item{
  width: 15vh;
  height: 15vh;
  border: 0.2vh solid #2b64aa30;
  margin: 0.8vh;
}

</style>