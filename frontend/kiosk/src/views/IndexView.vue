<template>
  <div>
    <!-- Admin -->
    <div
      class="w-100 d-flex justify-content-between"
      @click="$router.push({ name: 'login' })"
      style="cursor: pointer"
    >
      <div></div>
      <div style="padding: 2.2vh">
        <font-awesome-icon
          icon="fa-solid fa-user"
          style="font-size: 4vh; margin: 1.5vh; margin-bottom: 0"
        />
        <div>관리자</div>
      </div>
    </div>

    <div
      class="d-flex flex-column justify-content-between"
      style="padding: 5vh; padding-top: 0"
    >
      <!-- LOGO -->
      <div>
        <img src="/logo.png" alt="Logo" style="height: 22vh" />
        <p style="font-size: 4vh">키오초등학교</p>
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
  width: 70%;
  padding: 1.5vh 0;
  margin: 3.5vh 0;
  font-size: 5vh;
  font-family: 'standard';
  font-weight: bold;
  color: white;
  background-color: #ffa946;
  border-radius: 5vh;
}
</style>
