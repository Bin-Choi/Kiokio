<template>
  <div>
    <!-- Display Input -->
    <div class="m-4">
      <span>학년/반/번호</span>
      <input type="text" v-model.trim="number" maxlength="6" minlength="6"
       class="rounded bg-light m-2">
    </div>

    <!-- SUBMIT BUTTON-->
    <button type="button" class="btn btn-primary " @click="submit"></button>

    <!-- Back -->
    <div class="w-25 d-flex mx-2 align-items-center" @click="$router.go(-1)">
      <font-awesome-icon icon="fa-solid fa-arrow-left" /> 뒤로가기
    </div>

    <!-- Keypad -->
    <table class="w-100 fixed-bottom">
      <tr class="row">
        <td class="col" @click="input(1)">1</td>
        <td class="col" @click="input(2)">2</td>
        <td class="col" @click="input(3)">3</td>
      </tr>
      <tr class="row">
        <td class="col" @click="input(4)">4</td>
        <td class="col" @click="input(5)">5</td>
        <td class="col" @click="input(6)">6</td>
      </tr>
      <tr class="row">
        <td class="col" @click="input(7)">7</td>
        <td class="col" @click="input(8)">8</td>
        <td class="col" @click="input(9)">9</td>
      </tr>
      <tr class="row">
        <td class="col" @click="input('.')">.</td>
        <td class="col" @click="input(0)">0</td>
        <td class="col" @click="del">지우기</td>
      </tr>
    </table>
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
table {
  background-color: #D9D9D9;
}

table td{
  display:flex;
  justify-content: center;
  align-items: center;
  border: 2px solid white;
  font-size: 60px;
  font-weight: bold;
  height: 180px;
}

input{
  text-align:center;
  width: 500px;
  height: 120px;
  box-shadow: 5px 5px 7px rgb(198, 207, 226); 
  border: none;
}

input:focus{
  outline:none;
}

button {
  box-shadow: 0 7px 7px rgba(17, 61, 147, 0.987); 
}
</style>