<template>
  <!-- Keypad -->
  <div class="d-flex flex-column">
    <div class="row">
      <div
        class="col"
        @click="input('1')"
        @touchstart="clicked"
        @touchend="unclicked"
      >
        1
      </div>
      <div
        class="col"
        @click="input('2')"
        @touchstart="clicked"
        @touchend="unclicked"
      >
        2
      </div>
      <div
        class="col"
        @click="input('3')"
        @touchstart="clicked"
        @touchend="unclicked"
      >
        3
      </div>
    </div>
    <div class="row">
      <div
        class="col"
        @click="input('4')"
        @touchstart="clicked"
        @touchend="unclicked"
      >
        4
      </div>
      <div
        class="col"
        @click="input('5')"
        @touchstart="clicked"
        @touchend="unclicked"
      >
        5
      </div>
      <div
        class="col"
        @click="input('6')"
        @touchstart="clicked"
        @touchend="unclicked"
      >
        6
      </div>
    </div>
    <div class="row">
      <div
        class="col"
        @click="input('7')"
        @touchstart="clicked"
        @touchend="unclicked"
      >
        7
      </div>
      <div
        class="col"
        @click="input('8')"
        @touchstart="clicked"
        @touchend="unclicked"
      >
        8
      </div>
      <div
        class="col"
        @click="input('9')"
        @touchstart="clicked"
        @touchend="unclicked"
      >
        9
      </div>
    </div>
    <div class="row">
      <div
        class="col"
        @click="input('.')"
        @touchstart="clicked"
        @touchend="unclicked"
      >
        .
      </div>
      <div
        class="col"
        @click="input('0')"
        @touchstart="clicked"
        @touchend="unclicked"
      >
        0
      </div>
      <div class="col" @click="del" @touchstart="clicked" @touchend="unclicked">
        &larr;
      </div>
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
    clicked(event) {
      event.srcElement.classList.add('clicked')
    },
    unclicked(event) {
      event.srcElement.classList.remove('clicked')
    },
  },
}
</script>

<style scoped>
.row {
  margin: 1vh auto;
  width: 75%;
  height: 100%;
}
.col {
  font-size: 2.7vh;
  font-weight: bold;

  margin: 0 1.3vh;
  border-radius: 3vh;
  border: 0.3vh solid #ff9900;
  color: #ff9900;
  padding: 0.5vh;

  box-shadow: 0 0.1vh 0.1vh #ff9900;
}
.clicked {
  background-color: #ff9900;
  color: white;
}
</style>
