<template>
  <div class="pt-5">
    <modal-pw-view v-if="showModal" />

    <div
      id="title"
      class="w-75 m-auto bg-primary rounded text-light p-1"
      style="font-size: 90px"
    >
      인바디 등록/조회
    </div>

    <info-view />
    <keypad-view v-if="!showModal" @show-pw-modal="showModal = true" />
  </div>
</template>

<script>
import InfoView from "@/components/InfoView.vue"
import KeypadView from "@/components/KeypadView.vue"
import ModalPwView from "../components/ModalPwView.vue"

export default {
  name: "InbodyView",
  components: {
    InfoView,
    KeypadView,
    ModalPwView,
  },
  data() {
    return {
      showModal: false,
    }
  },
}
</script>

<style></style>
