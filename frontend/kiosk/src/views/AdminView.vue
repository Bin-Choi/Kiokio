<template>
  <div class="p-5">
    <div class="d-flex flex-column align-items-end">
      <font-awesome-icon icon="fa-solid fa-house" />
      <span>키오스크 홈</span>
    </div>

    <div class="my-5">00초등학교 학생 정보 관리자 페이지</div>
    <!-- 로그인 -->
    <div class="bg-light w-50 p-5 m-auto rounded shadow">
      <div class="mt-3">
        <span>아이디 </span>
        <input type="text" class="shadow rounded" />
      </div>
      <div class="m-4">
        <span> 비밀번호 </span>
        <input type="password" class="shadow rounded" />
      </div>
      <div>
        <button type="button" class="btn btn-primary shadow">완료</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AdminView",
}
</script>

<style></style>
