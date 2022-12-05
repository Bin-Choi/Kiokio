<template>

  <div id="attend" class="w-100 h-100 d-flex flex-column justify-content-end">
    <modal-view v-if="showModal" @close-modal="showModal=false"/>

    <!-- PAGE TITLE -->
    <div id="title" class="w-75 bg-primary m-auto rounded text-light p-1 shadow" style="font-size: 3em;">
      출석체크
    </div>

    <!-- INFO -->
    <info-view/>

    <div class="d-flex align-items-center justify-content-center my-5">
      <!-- INPUT -->
      <input type="text" v-model.trim="num" maxlength="6" minlength="6"
        class="w-50 rounded bg-light p-4 m-3" style="font-size:2em">
      
      <!-- SUBMIT -->
      <button type="button" class="btn btn-primary btn-sm px-3 py-2 shadow m-3" 
      @click="submit">확인</button>
    </div>

    <div class="w-25 d-flex m-4 align-items-center" @click="$router.go(-1)" style="font-size:1.7em;">
      <font-awesome-icon icon="fa-solid fa-arrow-left" /> 뒤로가기
    </div>

    <!-- KEYPAD -->
    <keypad-view @val='modifyNum'/>
  
  </div>
</template>

<script>
import InfoView from '@/components/InfoView.vue'
import KeypadView from '@/components/KeypadView.vue'
import ModalView from '@/components/ModalView.vue'

export default {
  name:'AttendView',
  components: {
    InfoView,
    KeypadView,
    ModalView,
  },
  data(){
    return {
      num: '',
      showModal:false,
    }
  },
  methods: {
    // Submit Event
    submit(){
      // check the input length
      if (!this.num || this.num.length != 6){
        alert('학년 반 번호를 정확히 입력해주세요')
        return false
      }

      this.showModal = true
    },
    modifyNum(params){
      console.log(params)
    }
  }
}
</script>

<style >
input{
  text-align:center;
  border: none;
}

input:focus{
  outline:none;
}

#attend button,
#inbody button{
  font-size: 2em;
}
</style>