<template>
    <!-- Keypad -->
  <div class="d-flex flex-column keypad">
    <div class="row">
      <div class="col" @click="input(1)">1</div>
      <div class="col" @click="input(2)">2</div>
      <div class="col" @click="input(3)">3</div>
    </div>
    <div class="row">
      <div class="col" @click="input(4)">4</div>
      <div class="col" @click="input(5)">5</div>
      <div class="col" @click="input(6)">6</div>
    </div>
    <div class="row">
      <div class="col" @click="input(7)">7</div>
      <div class="col" @click="input(8)">8</div>
      <div class="col" @click="input(9)">9</div>
    </div>
    <div class="row">
      <div class="col" @click="input('.')">.</div>
      <div class="col" @click="input(0)">0</div>
      <div class="col" @click="input('del')">지우기</div>
    </div>
  </div>
</template>

<script>
export default {
  name:"KeypadView",
  data(){
    return {
      inputData:'',
    }
  },
  methods:{
    
    // INPUT NUMBER
    input(num){
      if (this.inputData.length < 6) {
        this.inputData += `${num}`
      }
    },
    // DELETE NUMBER
    del(){
      if (this.number.length > 0){
        this.number = this.number.slice(0, -1)
      }
    }
  }
  
}
</script>

<style scoped>
.keypad {
  background-color: #D9D9D9;
}

.row {
  width:100%;
}

.col {
  font-size: 1.7em;
  padding: 0.6em;
}
</style>