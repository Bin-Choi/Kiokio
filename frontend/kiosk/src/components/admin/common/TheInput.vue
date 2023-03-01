<template>
  <div :class="display">
    <label for="input">{{ label }}</label>
    <input
      :type="type"
      :min="min"
      :max="max"
      id="input"
      :ref="refer"
      v-model.trim="value"
      @keyup.enter="submit"
      @change="$emit('change', value)"
    />
  </div>
</template>

<script>
export default {
  name: 'TheInput',
  props: {
    type: {
      type: String,
      default: 'text',
    },
    min: {
      type: Number,
      default: undefined,
    },
    max: {
      type: Number,
      default: undefined,
    },
    refer: {
      type: String,
      default: null,
    },
    submit: {
      type: Function,
      default: undefined,
    },
    label: {
      type: String,
      default: null,
    },
    display: {
      type: String,
      default: null,
    },
  },
  data() {
    return {
      value: null,
    }
  },
}
</script>

<style scoped>
div {
  display: flex;
  align-items: center;
}

input {
  background-color: white;
  margin: 0 1.5vh 0 0.5vh;
  width: 10vh;
  height: 3.5vh;
  border-radius: 1vh;
}

.right {
  flex-direction: row-reverse;
}

.long > input {
  width: 13vh;
}
</style>
