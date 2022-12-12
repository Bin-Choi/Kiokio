<template>
  <div style="padding: 7vh">
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
      <div class="d-flex flex-column align-items-center">
        <div class="button shadow" @click="$router.push({ name: 'attend' })">
          출석체크
        </div>

        <div class="button shadow" @click="$router.push({ name: 'inbody' })">
          인바디
        </div>

        <div class="button shadow" @click="$router.push({ name: 'gym' })">
          운동기구
        </div>
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
.button {
  width: 60%;
  padding: 2vh;
  margin: 3.5vh 0;
  font-size: 5vh;
  font-family: 'bold';
  color: white;
  background-color: #ffa946;
  border-radius: 5vh;
  /* border: 0.5vh double #f6f6f6; */
}
</style>
