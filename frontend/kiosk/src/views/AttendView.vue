<template>

  <div class="attend d-flex flex-column justify-content-between">
    <modal-view v-if="showModal" @close-modal="showModal=false"/>

    <div id="title" class="w-75 bg-primary m-auto rounded text-light p-1" style="font-size: 90px;">
      출석체크
    </div>

    <info-view/>

    <input type="text" v-model.trim="number" maxlength="4" minlength="4"
      class="w-50 rounded bg-light m-auto">

    <keypad-view v-if="!showModal" @show-modal="showModal=true"/>
  
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
      showModal:false,
    }
  }
}
</script>

<style scoped>
.attend{
  height: 100vh;
}
input{
  text-align:center;
  height:5em;
  box-shadow: 5px 5px 7px rgb(198, 207, 226); 
  border: none;
}

input:focus{
  outline:none;
}
</style>