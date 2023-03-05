<template>
  <div :class="display">
    <label :for="refer">{{ label }}</label>
    <input
      :type="type"
      :min="min"
      :max="max"
      :id="refer"
      :ref="refer"
      :value="value"
      @keyup.enter="submit"
      @change="onChange"
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
    value: {
      type: String,
      default: null,
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
  methods: {
    onChange(e) {
      this.$emit('change', e.target.value)
    },
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
