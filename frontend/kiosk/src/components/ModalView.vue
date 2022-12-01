<template>
  <div class="modal-bg">
    <div class="modal-content m-auto rounded p-2">
      <div
        id="title"
        class="w-75 m-auto bg-primary rounded text-light p-1"
        style="font-size: 80px"
      ></div>

      <!-- ATTEND CONTENT -->
      <span
        v-if="$route.name === 'attend'"
        class="w-75 h-75 bg-light m-auto rounded d-flex flex-column align-items-center justify-content-evenly"
      >
        <div>
          <div>Time</div>
          <div>Class</div>
          <div>Name</div>
        </div>

        <div class="d-flex flex-column w-50">
          <button type="button" class="btn btn-success mb-2" @click="attend">
            출석하기
          </button>
          <button
            type="button"
            class="btn btn-danger"
            @click="$emit('close-modal')"
          >
            취소
          </button>
        </div>
      </span>

      <!-- GYM CONTENT -->
      <span
        v-if="$route.name === 'gym'"
        class="w-75 h-75 bg-light m-auto rounded d-flex flex-column align-items-center justify-content-between py-3"
      >
        <img src="#" alt="IMG" />
        <div>description</div>
        <button
          id="title"
          type="button"
          class="btn btn-primary btn-md btn-block"
          @click="$emit('close-modal')"
        >
          확인
        </button>
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: "ModalView",
  methods: {
    attend() {
      // send attendance data

      // and close modal view
      this.$emit("close-modal")
    },
  },
  mounted() {
    const title = document.querySelector(".modal-content #title")
    if (this.$route.name == "gym") {
      title.innerText = "운동기구 이름"
    } else {
      title.innerText = "출석 확인"
    }
  },
}
</script>

<style scoped>
.modal-bg {
  display: flex;
  align-items: center;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.432);
  position: fixed;
  top: 0;
}

.modal-content {
  width: 80%;
  height: 60%;
  background-color: #e7f1ff;
}
</style>
