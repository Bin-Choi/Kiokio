<template>
  <div
    class="d-flex flex-column align-items-center"
    style="width: 100vw; height: 100vh; padding: 7vh">
    <div class="d-flex justify-content-between w-100">
      <div @click="$router.push({ name: 'index' })" style="cursor: pointer">
        <font-awesome-icon icon="fa-solid fa-house" />
        <span>키오스크 홈</span>
      </div>
      <div @click="$store.dispatch('logout')" style="cursor: pointer">
        <font-awesome-icon icon="fa-solid fa-user" />
        <span>로그아웃</span>
      </div>
    </div>

    <div
      class="bg-secondary rounded shadow d-flex flex-column"
      style="width: 100%; height: 80vh; padding: 3vh; margin-top: 5vh">
      <div class="d-flex justify-content-between">
        <div>
          <span>학년</span>
          <input
            type="number"
            class="student-search-form"
            ref="grade"
            v-model="grade"
            @keyup.enter="$refs.room.focus()" />
          <span>반</span>
          <input
            type="number"
            class="student-search-form"
            ref="room"
            v-model="room"
            @keyup.enter="$refs.number.focus()" />
          <span>번호</span>
          <input
            type="number"
            class="student-search-form"
            ref="number"
            v-model="number"
            @keyup.enter="$refs.name.focus()" />
          <span>이름</span>
          <input
            type="text"
            class="student-search-form"
            ref="name"
            v-model="name"
            @keyup.enter="$refs.password.focus()" />
          <button class="student-search-btn" @click="searchStudents">
            조회
          </button>
        </div>
        <button
          class="student-add-btn"
          @click="$router.push({ name: 'studentCreate' })">
          + 학생 추가
        </button>
      </div>
      <div></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'StudentView',
  data() {
    return {
      grade: null,
      room: null,
      number: null,
      name: null,
    }
  },
  methods: {},
}
</script>

<style scoped>
.student-search-btn {
  background-color: rgb(28, 75, 163);
  width: 10vw;
  height: 5vh;
  border-radius: 1vh;

  color: white;
  line-height: 5vh;
  font-size: 2vh;
  font-weight: bold;
}
.student-search-form {
  background-color: white;
  width: 10vw;
  height: 4vh;
  border-radius: 1vh;
}
.student-add-btn {
  background-color: rgb(109, 163, 28);
  width: 10vw;
  height: 5vh;
  border-radius: 1vh;

  color: white;
  line-height: 5vh;
  font-size: 2vh;
  font-weight: bold;
}
</style>
