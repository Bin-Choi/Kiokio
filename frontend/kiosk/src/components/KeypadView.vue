<template>
  <div>
    <!-- Display Input -->
    <div class="my-3">
      <span>학년/반/번호</span>
      <input type="text" v-model="number" maxlength="6" minlength="6"
       class="rounded bg-light m-2">
    </div>

    <!-- Submit Button -->
    <button type="button" class="btn btn-primary ">Primary</button>

    <!-- Keypad -->
    <table class="w-100 fixed-bottom mb-5">
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
</style>