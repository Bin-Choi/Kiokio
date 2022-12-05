<template>
  <div class="h-100 d-flex flex-column justify-content-between">

    <modal-view v-if="showModal" @close-modal="(showModal=false)"/>

    <div class="w-75 m-auto bg-primary rounded text-light p-1 shadow" style="font-size: 3em;">
      운동기구 사용법
    </div>
    
    <scroll-view @show-modal="showModal=true"/>

    <!-- BACK -->
    <div class="d-flex m-5 align-items-center" style="font-size:2em;"
    @click="$router.go(-1)">
      <font-awesome-icon icon="fa-solid fa-arrow-left" /> 뒤로가기
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