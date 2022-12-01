<template>
  <div class="modal-bg">
    <div class="modal-content m-auto rounded">
      <div id="title" class="w-75 m-auto bg-primary rounded text-light p-1" style="font-size: 80px;">
      비밀번호 입력
      </div>

      <input type="text" v-model.trim="number" maxlength="4" minlength="4"
      class="w-75 m-auto rounded my-0">

      <button type="button" class="w-25 btn btn-primary btn-sm m-auto" @click="submit">입력</button>


      <!-- Keypad -->
      <table class="w-100 rounded">
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
          <td class="col" @click="input('.')" style="border-radius: 0 0 0 20px;">.</td>
          <td class="col" @click="input(0)">0</td>
          <td class="col" @click="del" style="border-radius: 0 0 20px 0;">지우기</td>
        </tr>
      </table>
        

    </div>
  </div>
</template>

<script>

export default {
  name:'ModalPwView',
  data(){
    return {
      number: '',
    }
  },
  methods:{
    // INPUT NUMBER
    input(num){
      if (this.number.length < 4) {
        this.number += `${num}`
      }
    },
    // DELETE NUMBER
    del(){
      if (this.number.length > 0){
        this.number = this.number.slice(0, -1)
      }
    },
    // SUBMIT PASSWORD
    submit(){
      // check the input length
      if (!this.number || this.number.length != 4){
        alert('비밀번호를 정확히 입력해주세요')
        return false
      }
      
      this.$router.push({name:'inbodyDetail'})
    }
  }
}
</script>

<style scoped>
.modal-bg{
  display: flex;
  align-items: center;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.432);
  position: fixed;
  top: 0;
}

.modal-content{
  width: 80%;
  height: 60%;
  background-color: #e7f1ff;
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
  height: 140px;
}

.row {
  --bs-gutter-x: 0;
}

button {
  box-shadow: 0 7px 7px rgba(17, 61, 147, 0.987); 
}
</style>