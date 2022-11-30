<template>
  <div>
    <!-- Display Input -->
    <div class="my-3">
      <span>학년/반/번호</span>
      <input type="text" v-model="number" maxlength="6" minlength="6"
       class="rounded bg-light m-2">
    </div>

    <!-- Submit Button -->
    <button type="button" class="btn btn-primary "></button>

    <!-- Back -->
    <div class="w-25 d-flex mx-2 align-items-center" @click="$router.go(-1)">
      <font-awesome-icon icon="fa-solid fa-arrow-left" /> 뒤로가기
    </div>

    <!-- Keypad -->
    <table class="w-100 fixed-bottom">
      <tr class="row">
        <td class="col">1</td>
        <td class="col">2</td>
        <td class="col">3</td>
      </tr>
      <tr class="row">
        <td class="col">4</td>
        <td class="col">5</td>
        <td class="col">6</td>
      </tr>
      <tr class="row">
        <td class="col">7</td>
        <td class="col">8</td>
        <td class="col">9</td>
      </tr>
      <tr class="row">
        <td class="col">.</td>
        <td class="col">0</td>
        <td class="col">지우기</td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name:"KeypadView",
  data(){
    return {
      number:null,
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