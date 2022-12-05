<template>
  <div id="inbody" class="w-100 h-100 d-flex flex-column justify-content-end">
    <modal-pw-view v-if="showModal" />
    
    <div
      id="title"
      v-if="!showModal"
      class="w-75 m-auto bg-primary rounded text-light p-1 shadow"
      style="font-size: 3em"
    >
      인바디 등록/조회
    </div>

    <!-- INFO -->
    <info-view 
    v-if="!showModal"/>

    <div v-if="!showModal" class="d-flex align-items-center justify-content-center my-5">
      <!-- INPUT -->
      <input type="text" v-model.trim="num" maxlength="6" minlength="6"
        class="w-50 rounded bg-light p-4" style="font-size:2em">

      <!-- SUBMIT -->
      <button type="button" class="btn btn-primary btn-sm px-3 py-2 shadow m-3" 
      @click="submit">확인</button>
    </div>

    <!-- BACK -->
    <div v-if="!showModal" class="w-25 d-flex m-4 align-items-center" @click="$router.go(-1)" style="font-size:1.7em;">
      <font-awesome-icon icon="fa-solid fa-arrow-left" /> 뒤로가기
    </div>

    <!-- KEYPAD -->
    <keypad-view @show-pw-modal="showModal = true" />

  </div>
</template>

<script>
import InfoView from "@/components/InfoView.vue"
import KeypadView from "@/components/KeypadView.vue"
import ModalPwView from "../components/ModalPwView.vue"

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
      this.showModal = true
    }
  }
}
</script>

<style></style>
