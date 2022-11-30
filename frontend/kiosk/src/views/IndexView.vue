<template>
  <div class="p-4">
    <!-- Admin -->
    <div class="d-flex flex-column align-items-end m-2">
      <font-awesome-icon icon="fa-solid fa-user" class="fa-2x m-2 mb-0"/>
      <span >관리자</span>
    </div>

    <!-- Logo Img & Slogan -->
    <div class="m-5">
      <img src="#" alt="Logo">
      <h1>딩초초등학교</h1>
    </div>

    <!-- Buttons -->
    <div class="d-flex flex-column m-4">
      <button type="button" class="btn btn-primary btn-lg btn-block "
      @click="$router.push('attend')">출석체크</button>
      <button type="button" class="btn btn-primary btn-lg btn-block">인바디</button>
      <button type="button" class="btn btn-primary btn-lg btn-block">운동기구</button>
    </div>
  </div>
</template>

<script>

export default {
  name: 'IndexView',
}
</script>

<style scoped>

button {
  padding: 35px;
  margin-bottom: 100px;
  font-size: 80px;
  box-shadow: 0 7px 7px rgb(6, 43, 116); 
}

</style>