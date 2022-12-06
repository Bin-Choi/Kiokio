<template>
  <div id="inbody" class="w-100 h-100 d-flex flex-column justify-content-end">


    <!-- MODAL -->
    <modal-pw-view v-if="showModal"/>

    <!-- BACK -->

    <div class="w-25 d-flex align-items-center" @click="$router.go(-1)" style="font-size:4.5vh; margin: 3vh; margin-bottom:0;">
      <font-awesome-icon icon="fa-solid fa-circle-arrow-left" />
    </div>

    <div class="h-50 d-flex flex-column align-items-center justify-conent-around">
    <!-- PAGE TITLE -->
    <div
      id="title"
      v-if="!showModal"
      class="w-75 m-auto bg-primary rounded text-light p-1 shadow"
      style="font-size: 5vh;"
    >
      인바디 등록/조회
    </div>

    <!-- INFO -->
    <info-view 
    v-if="!showModal"/>

    <div v-if="!showModal" class="d-flex align-items-center justify-content-center my-5">
      <!-- INPUT -->
      <input type="text" v-model.trim="num" maxlength="5" minlength="5"
        class="w-50 rounded bg-light p-4" style="font-size:2em">

      <!-- SUBMIT -->
      <button type="button" class="btn btn-primary btn-sm px-3 py-2 shadow m-3" 
      @click="submit">확인</button>
    </div>
  </div>



    <!-- KEYPAD -->
    <keypad-view @show-pw-modal="showModal = true" />

  </div>
</template>

<script>
import InfoView from "@/components/InfoView.vue"
import KeypadView from "@/components/KeypadView.vue"
import ModalPwView from "../components/ModalPwView.vue"

import axios from 'axios'

export default {
  name: "InbodyView",
  components: {
    InfoView,
    KeypadView,
    ModalPwView,
  },
  data() {
    return {
      num:'',
      showModal: false,
    }
  },
  methods:{
    submit(){
      // CHECK INPUT FORM
      if (!this.num || this.num.length != 5){
        alert('학년 반 번호를 정확히 입력해주세요')
        return false
      }

      const URL = "http://127.0.0.1:8000"
      axios({
        method:'get',
        url: `${URL}/students/inbody/`,
        data: {
          number: this.num,
        }
      })

      .then((res)=>{
        this.$store.commit('STUDENT_INFO', res.data);
        this.showModal = true
      })

      .catch((err)=>{
        alert('없는 번호입니다.')
        console.log(err)
      })

      this.num = ''

    }
  }
}
</script>

<style></style>
