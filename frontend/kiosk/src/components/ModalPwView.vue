<template>
  <div class="modal-bg">
    
    <div class="modal-content m-auto rounded shadow py-5">
      <div id="title" class="w-75 m-auto bg-primary rounded text-light p-1 shadow" style="font-size: 2em;">
      비밀번호 입력
      </div>

      <div class="w-75 h-75 py-5 m-auto rounded shadow bg-light d-flex flex-column justify-content-evenly align-items-center">
        <input type="password" v-model.trim="number" maxlength="4" minlength="4"
        class="w-50 rounded p-3" style="font-size:1.5em">

        <button type="button" class="w-50 btn btn-primary btn-sm shadow" style="font-size:1.5em;"
        @click="submit">확인</button>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name:'ModalPwView',
  methods:{
    // SUBMIT PASSWORD
    submit(){
      
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
  position: fixed;
  top: 0;
}

.modal-content{
  width: 90%;
  height: 50%;
  bottom:20%;
}

input {
  background-color: #2b64aa1e;
}


</style>