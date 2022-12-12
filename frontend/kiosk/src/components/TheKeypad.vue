<template>
  <!-- Keypad -->
  <div class="d-flex flex-column keypad">
    <div class="row">
      <div class="col" @click="input('1')">1</div>
      <div class="col" @click="input('2')">2</div>
      <div class="col" @click="input('3')">3</div>
    </div>
    <div class="row">
      <div class="col" @click="input('4')">4</div>
      <div class="col" @click="input('5')">5</div>
      <div class="col" @click="input('6')">6</div>
    </div>
    <div class="row">
      <div class="col" @click="input('7')">7</div>
      <div class="col" @click="input('8')">8</div>
      <div class="col" @click="input('9')">9</div>
    </div>
    <div class="row">
      <div class="col" @click="input('.')">.</div>
      <div class="col" @click="input('0')">0</div>
      <div class="col" @click="del">&larr;</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TheKeypad',
  methods: {
    // INPUT NUMBER
    input(value) {
      this.$emit('input', value)
    },
    // DELETE NUMBER
    del() {
      this.$emit('del')
    },
  },
}
</script>

<style scoped>
.keypad {
  font-size: 3vh;
  font-weight: bold;
}
.row {
  margin: 1vh auto;
  width: 75%;
  height: 100%;
}
.col {
  font-size: 3vh;
  margin: 0 1vh;
  border-radius: 4vh;
  border: 0.3vh solid #ff9900;
  color: #ff9900;
  padding: 1vh;
}

.col:active {
  background-color: #ff9900;
  color: white;
}
</style>
