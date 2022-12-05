<template>
  <div>
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
        <div class="col" @click="del">지우기</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name:"KeypadView",
  data(){
    return {
      number:'',
      password:null,
    }
  },
  // Button InnerText
  mounted(){
    const btn = document.querySelector('button')
    if (this.$route.name == 'inbody'){
      btn.innerText = '조회하기'
    } else {
      btn.innerText = '출석하기'
    }
  },
  methods:{
    // Submit Event
    submit(){
      // check the input length
      if (!this.number || this.number.length != 6){
        alert('학년 반 번호를 정확히 입력해주세요')
        return false
      }

      // submit logic according to route name
      if (this.$route.name == 'inbody'){
        this.$emit('show-pw-modal')
      } else {
        console.log(this.number)
        this.$emit('show-modal')
      }

    },
    // INPUT NUMBER
    input(num){
      if (this.number.length < 6) {
        this.number += `${num}`
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

.col {
  font-size: 1.65em;
  padding: 0.5em;
}

button {
  box-shadow: 0 7px 7px rgba(17, 61, 147, 0.987); 
}
</style>