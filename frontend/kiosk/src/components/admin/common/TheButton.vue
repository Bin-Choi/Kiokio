<template>
  <button :class="color" @click="onClick">
    {{ text }}
  </button>
</template>

<script>
export default {
  name: 'TheButton',
  props: {
    color: {
      type: String,
      default: 'blue',
    },
    text: {
      type: String,
      default: null,
      required: true,
    },
    onClick: {
      type: Function,
      default: undefined,
    },
  },
}
</script>

<style scoped>
button {
  width: fit-content;
  height: 3.5vh;
  border-radius: 1vh;
  border: 0;
  color: white;
  font-size: 1.8vh;
}

.green {
  background-color: rgb(109, 163, 28);
}
.red {
  background-color: rgb(193, 32, 42);
}
.blue {
  background-color: #6396c3;
}
.gray {
  background-color: rgb(121, 121, 121);
}
</style>
