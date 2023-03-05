<template>
  <div @click="onClick">
    <font-awesome-icon :icon="icon" />
    <span>{{ text }}</span>
  </div>
</template>

<script>
export default {
  name: 'IconButon',
  props: {
    icon: {
      type: String,
      required: true,
    },
    text: {
      type: String,
      default: null,
    },
    onClick: {
      type: Function,
      default: undefined,
    },
  },
}
</script>

<style scoped>
div {
  display: flex;
  flex-direction: column;

  font-size: 3vh;
  cursor: pointer;
}

span {
  font-size: 1.5vh;
}
</style>
