<template>
  <div class="h-100 d-flex flex-column justify-content-between">
    <!-- MODAL -->
    <modal-view v-if="showModal" @close-modal="showModal=false" :student="this.student"/>

    <!-- BACK -->
    <div class="d-flex" @click="$router.go(-1)" style="font-size:4.5vh; margin: 3vh; margin-bottom:0;">
        <font-awesome-icon icon="fa-solid fa-circle-arrow-left" />
    </div>

    <div class="h-50 d-flex flex-column align-items-center justify-content-around">

      <!-- PAGE TITLE -->
      <div class="w-75 bg-primary rounded text-light shadow" style="font-size: 5vh;">
        출석체크
      </div>

      <!-- INFO -->
      <info-view/>            

      <div class="d-flex align-items-center justify-content-center">
        <!-- INPUT -->
        <input type="text" v-model.trim="num" maxlength="5" minlength="5"
          class="w-50 rounded bg-light" style=" padding: 1vh; margin-right: 2vh; font-size:3vh;">
        
        <!-- SUBMIT -->
        <button type="button" class="btn btn-primary shadow" style="font-size:3vh;"
        @click="submit">확인</button>
      </div>
    </div>

    <!-- KEYPAD -->
    <keypad-view/>
  
  </div>
</template>

<script>
import InfoView from '@/components/InfoView.vue'
import KeypadView from '@/components/KeypadView.vue'
import ModalView from '@/components/ModalView.vue'

import axios from 'axios'

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
      student:'',
      showModal:false,
    }
  },
  methods: {
    // Submit Event
    submit(){
      // check the input length
      if (!this.num || this.num.length != 5){
        alert('학년 반 번호를 정확히 입력해주세요')
        return false
      }

      // Check Num
      const URL = "http://127.0.0.1:8000"

      axios({
        method: 'get',
        url: `${URL}/students/${this.num}/attendance/`,
        data: {
          num: this.num,
        }
      })

      .then((res)=>{
        this.student = res.data
        this.showModal = true
      })

      .catch((err)=>{
        alert('없는 번호입니다.')
        console.log(err)
      })
      
      this.num = ''

      
    },

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

</style>