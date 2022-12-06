<template>
  <div class="w-75 bg-light rounded m-auto shadow" style="padding: 2.5vh 2vh;">
    <div id="scroll-box">

      <!-- display gym list if the router name is gym -->
      <span
        v-if="$route.name === 'gym'"
        class="d-flex flex-wrap justify-content-center"
      >
        <gym-item
          v-for="(gym, idx) in this.gyms"
          :key="idx"
          :gym="gym"
          @show-modal="$emit('show-modal')"
        />
      </span>

      <!-- display inbody record history if the router name is record history -->
      <!-- <span>

      </span> -->

      <inbody-detail v-if="$route.name === 'inbodyDetail'" />
    </div>
  </div>
</template>

<script>
import GymItem from "./GymItem.vue"
import InbodyDetail from "@/components/InbodyDetail.vue"

export default {
  name: "ScrollView",
  components: {
    InbodyDetail,
    GymItem,
  },
  data() {
    return {
      // temporary data
      gyms: ["gym1", "gym2", "gym3", "gym4", "gym5", "gym6", "gym7"],
    }
  },
}
</script>

<style scoped>

#scroll-box {
  height: 60vh;
  overflow: auto;
}

#scroll-box::-webkit-scrollbar {
  width: 1vh;
}
#scroll-box::-webkit-scrollbar-thumb {
  background-color: #0275d8;
  border-radius: 0.5vh;
}
#scroll-box::-webkit-scrollbar-track {
  border-radius: 0.5vh;
  border: 0.2vh solid #2b64aa1e;
}

#scroll-box::-webkit-scrollbar-corner {
  display: none;
}
</style>
