<template>
  <div id="info-box" class="bg-white shadow round">
    <div class="font-weight-bold">학년, 반, 번호를 입력해주세요.</div>
    <div class="d-flex flex-column">
      <span> 예시) 1학년 1반 1번</span>
      <span><font-awesome-icon icon="fa-solid fa-arrow-right" /> 10101</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'InfoView',
}
</script>

<style scoped>
#info-box {
  padding: 3vh;
  font-size: 2.5vh;
}
</style>
