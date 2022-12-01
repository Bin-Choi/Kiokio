<template>
  <div class="item rounded m-2 p-auto" @click="$emit('show-modal')">
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
  width: 300px;
  height: 300px;
  border: 3px solid #2b64aa30;
  box-shadow: 2px 2px 3px #2b64aa30; 
}

</style>