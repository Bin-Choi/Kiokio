<template>
  <div class="w-75 bg-light rounded m-auto shadow" style="padding: 2.5vh 2vh">
    <div id="scroll-box">
      <!-- GYM -->
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

      <!-- INBODY DETAIL -->

      <!-- INBODY HISTORY -->
      <!-- <span>

      </span> -->
    </div>
  </div>
</template>

<script>
export default {
  name: 'ScrollView',
  components: {},
  data() {
    return {
      // temporary data
    }
  },
}
</script>

<style></style>
