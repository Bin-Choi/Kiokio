<template>
  <div class="modal-bg">
    <div class="modal-content m-auto rounded p-2 shadow">
      <div
        id="title" 
        class="w-75 m-auto bg-primary rounded text-light p-1 shadow"
        style="font-size: 80px"
      ></div>

      <!-- ATTEND CONTENT -->
      <span
        v-if="$route.name === 'attend'"
        class="w-75 h-75 bg-light m-auto rounded d-flex flex-column align-items-center justify-content-evenly"
      >
        <div style="font-size:1em;">
          <div>Time</div>
          <div>Class</div>
          <div>Name</div>
        </div>

        <div class="d-flex flex-column" style="font-size:0.7em;">
          <button type="button" class="btn btn-sm btn-success mb-3 px-5 shadow" @click="attend">
            출석하기
          </button>
          <button
            type="button"
            class="btn btn-danger btn-sm shadow"
            @click="$emit('close-modal')"
          >
            취소
          </button>
        </div>
      </span>

      <!-- GYM CONTENT -->
      <span
        v-if="$route.name === 'gym'"
        class="w-75 h-75 bg-light m-auto rounded d-flex flex-column align-items-center justify-content-between py-3 shadow"
      >
        <img src="#" alt="IMG" />
        <div>description</div>
        <button
          type="button"
          class="btn btn-primary btn-block shadow m-3 px-4 shadow" style="font-size:1em;"
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
