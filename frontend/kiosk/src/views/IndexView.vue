<template>
  <div id="index" class="p-5">
    <!-- Admin -->
    <div
      class="d-flex flex-column align-items-end m-5"
      @click="$router.push('admin')"
    >
      <font-awesome-icon icon="fa-solid fa-user" class="fa-2x m-2 mb-0" />
      <span>관리자</span>
    </div>

    <!-- Logo Img & Slogan -->
    <div class="m-5">
      <img src="#" alt="Logo" />
      <h1>딩초초등학교</h1>
    </div>

    <!-- Buttons -->
    <div class="d-flex flex-column m-5">
      <button
        type="button"
        class="btn btn-primary btn-lg btn-block shadow"
        @click="$router.push('attend')"
      >
        출석체크
      </button>

      <button
        type="button"
        class="btn btn-primary btn-lg btn-block shadow"
        @click="$router.push('inbody')"
      >
        인바디 등록/조회
      </button>

      <button
        type="button"
        class="btn btn-primary btn-lg btn-block shadow"
        @click="$router.push('gym')"
      >
        운동기구
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "IndexView",
}
</script>

<style scoped>
#index button {
  padding: 0.7em;
  margin: 1em 0;
  font-size: 2.2em;
}
</style>