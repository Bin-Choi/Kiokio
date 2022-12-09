<template>
  <div
    class="bg-white d-flex flex-column align-items-center"
    style="width: 100vw; height: 100vh; padding: 7vh"
  >
    <div class="d-flex justify-content-between w-100">
      <div
        @click="$store.dispatch('logout')"
        style="cursor: pointer"
        class="d-flex flex-column"
      >
        <font-awesome-icon icon="fa-solid fa-user" style="font-size: 3vh" />
        <span>로그아웃</span>
      </div>
      <div
        @click="$router.push({ name: 'index' })"
        class="d-flex flex-column"
        style="cursor: pointer"
      >
        <font-awesome-icon icon="fa-solid fa-house" style="font-size: 3vh" />
        <span>키오스크 홈</span>
      </div>
    </div>

    <div
      class="rounded shadow-sm d-flex flex-column w-75"
      style="
        height: 80vh;
        padding: 3vh;
        margin-top: 5vh;
        border: 0.5vh solid #2b64aa1e;
      "
    >
      <div class="d-flex justify-content-between">
        <div>
          <span>학년</span>
          <input
            type="number"
            class="rounded shadow-sm"
            ref="grade"
            v-model="grade"
            @keyup.enter="$refs.password.focus()"
          />
          <span>반</span>
          <input
            type="number"
            class="rounded shadow-sm"
            ref="grade"
            v-model="grade"
            @keyup.enter="$refs.password.focus()"
          />
          <span>번호</span>
          <input
            type="number"
            class="rounded shadow-sm"
            ref="grade"
            v-model="grade"
            @keyup.enter="$refs.password.focus()"
          />
          <span>이름</span>
          <input
            type="text"
            class="rounded shadow-sm"
            ref="grade"
            v-model="grade"
            @keyup.enter="$refs.password.focus()"
          />
        </div>
        <div
          class="btn btn-primary rounded shadow-sm font-weight-bold"
          @click="$router.push({ name: 'studentCreate' })"
        >
          + 학생 추가
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'StudentView',
  data() {
    return {
      grade: null,
    }
  },
  methods: {},
}
</script>

<style scoped>
input {
  font-size: 2vh;
  background-color: #2b64aa1e;
  width: 11vh;
  padding: 0.5vh;
  margin: 0 1vh;
}
</style>
