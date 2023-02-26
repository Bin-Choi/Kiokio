<template>
  <div>
    <TheModal v-if="showModal" @close-modal="showModal = false" />

    <kiosk-header />

    <div
      class="h-100 d-flex flex-column justify-content-between align-items-center"
    >
      <div class="w-75 title shadow" style="margin-top: 5vh">운동기구</div>
      <div
        class="w-75 bg-white round m-auto shadow"
        style="padding: 2.5vh 2vh; border: 0.1vh solid #ffa946"
      >
        <div id="scroll-box">
          <span
            v-if="$route.name === 'gym'"
            class="d-flex flex-wrap justify-content-center"
          >
            <gym-item
              v-for="(gym, idx) in this.gyms"
              :key="idx"
              :gym="gym"
              @show-modal="showModal = true"
            />
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import TheModal from '../components/TheModal.vue'
// import KioskHeader from '../components/KioskHeader.vue'
// import GymItem from '@/components/kiosk/gym/GymItem.vue'

import TheModal from '@/components/kiosk/common/TheModal.vue'
import KioskHeader from '@/components/kiosk/common/KioskHeader.vue'
import GymItem from '@/components/kiosk/gym/GymItem.vue'

export default {
  name: 'GymView',
  components: {
    KioskHeader,
    GymItem,
    TheModal,
  },
  data() {
    return {
      showModal: false,
      gyms: [
        {
          title: '런닝머신',
          photo: '/gym/treadmill.jpg',
          detail: '운동기구 설명',
        },
        { title: '스테퍼', photo: '/gym/stepper.jpg', detail: '운동기구 설명' },
        { title: '레그컬', photo: '/gym/legcurl.jpg', detail: '운동기구 설명' },
        {
          title: '체스트프레스',
          photo: '/gym/체스트프레스.jpg',
          detail: '운동기구 설명',
        },
      ],
    }
  },
}
</script>

<style></style>
