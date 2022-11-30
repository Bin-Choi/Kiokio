<template>
  <div class="pt-5">
    <info-view/>
    <keypad-view/>
  </div>
</template>

<script>
import InfoView from '@/components/InfoView.vue'
import KeypadView from '@/components/KeypadView.vue'

export default {
  name:'AttendView',
  components: {
    InfoView,
    KeypadView,
  }
}
</script>

<style>

</style>