<template>
  <div>
    <modal-view v-if="showModal" @close-modal="(showModal=false)"/>

    <!-- BACK -->
    <div class="d-flex" @click="$router.go(-1)" style="font-size:4.5vh; margin: 3vh; margin-bottom:0;">
        <font-awesome-icon icon="fa-solid fa-circle-arrow-left" />
    </div>


    <div class="h-100 d-flex flex-column justify-content-between align-items-center">
      <div class="w-75 bg-primary rounded text-light shadow" style="font-size: 5vh; margin-top:5vh;">
        운동기구
      </div>
      <scroll-view @show-modal="showModal=true"/>
    </div>
  </div>
</template>

<script>
import ScrollView from '../components/ScrollView.vue';
import ModalView from '../components/ModalView.vue';

export default {
  name:'GymView',
  components: {
    ScrollView,
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