<template>
  <div class="pt-5">
    <div id="title" class="w-75 m-auto bg-primary rounded text-light p-1" style="font-size: 90px;">
      인바디 등록/조회
    </div>

    <info-view/>
    <keypad-view/>
  </div>
</template>

<script>
import InfoView from '@/components/InfoView.vue'
import KeypadView from '@/components/KeypadView.vue'

export default {
  name:'InbodyView',
  components: {
    InfoView,
    KeypadView,
  }
}
</script>

<style>

</style>