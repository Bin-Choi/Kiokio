<template>
  <div class="pt-5">
    <modal-view v-if="showModal" @close-modal="showModal=false"/>

    <div id="title" class="w-75 m-auto bg-primary rounded text-light p-1" style="font-size: 90px;">
      출석체크
    </div>

    <info-view/>
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

<style>

</style>