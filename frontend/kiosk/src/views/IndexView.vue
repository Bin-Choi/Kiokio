<template>
  <div id="index" style="padding: 7vh">
    <!-- Admin -->
    <div
      class="w-100 d-flex flex-column align-items-end justify-content-center"
      @click="$router.push({ name: 'login' })"
    >
      <font-awesome-icon icon="fa-solid fa-user" style="font-size: 4vh" />
      <span>관리자</span>
    </div>

    <div class="d-flex flex-column justify-content-between">
      <!-- LOGO -->
      <div>
        <img src="#" alt="Logo" />
        <p style="font-size: 4vh">홍0초등학교</p>
      </div>

      <!-- Buttons -->
      <div class="d-flex flex-column">
        <button
          type="button"
          class="btn btn-primary btn-block shadow"
          @click="$router.push('attend')"
        >
          출석체크
        </button>

        <button
          type="button"
          class="btn btn-primary btn-block shadow"
          @click="$router.push('inbody')"
        >
          인바디
        </button>

        <button
          type="button"
          class="btn btn-primary btn-block shadow"
          @click="$router.push('gym')"
        >
          운동기구
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'IndexView',
}
</script>

<style scoped>
#index button {
  padding: 1.5vh;
  margin: 3.5vh 0;
  font-size: 5vh;
}
</style>
