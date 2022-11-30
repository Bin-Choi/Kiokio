<template>
  <div>
    <div id="info-box" class="w-75 bg-light m-auto p-2 mt-3 rounded">
    <div class="font-weight-bold">학년, 반, 번호를 입력해주세요.</div>
    <div class="d-flex flex-column mt-2">
      <span> 예시) 1학년 1반 1번</span>
      <span><font-awesome-icon icon="fa-solid fa-arrow-right"/> 010101</span>
    </div>
    </div>
  </div>
  
</template>

<script>
export default {
  name:'InfoView',
}
</script>

<style>
#info-box{
  box-shadow: 5px 5px 7px rgb(198, 207, 226); 
}

</style>