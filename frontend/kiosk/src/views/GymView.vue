<template>
  <div class="pt-5">

    <modal-view v-if="showModal" @close-modal="(showModal=false)"/>

    <div id="title" class="w-75 m-auto bg-primary rounded text-light p-1" style="font-size: 90px;">
      운동기구 사용법
    </div>
    
    <scroll-view @show-modal="showModal=true"/>

    <div class="w-25 d-flex m-4 align-items-center fixed-bottom" @click="$router.go(-1)">
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