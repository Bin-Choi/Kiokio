<template>
  <div class="d-flex justify-content-between">
    <div
      class="d-flex"
      @click="$router.go(-1)"
      style="font-size: 4vh; cursor: pointer">
      <font-awesome-icon icon="fa-solid fa-circle-arrow-left" />
    </div>
    <button v-if="!readyDelete" class="green-btn" @click="$emit('add-row')">
      행 추가
    </button>
    <button class="red-btn" @click="$emit('delete-row')">행 삭제</button>
    <button
      v-if="!readyDelete"
      class="blue-btn"
      @click="$emit('create-student')">
      저장
    </button>
  </div>
</template>

<script>
export default {
  name: 'StudentCreateHeader',
  props: {
    readyDelete: Boolean,
  },
}
</script>

<style scoped>
.green-btn {
  background-color: rgb(109, 163, 28);
  width: 10vw;
  height: 5vh;
  border-radius: 1vh;

  border: 0;
  outline: 0;

  color: white;
  font-size: 2vh;
  font-weight: bold;
}
.green-btn:focus {
  outline: 2px solid black;
}
.green-btn:hover {
  background-color: rgb(13, 81, 17);
}
.red-btn {
  background-color: rgb(193, 32, 42);
  width: 10vw;
  height: 5vh;
  border-radius: 1vh;

  border: 0;
  outline: 0;

  color: white;
  font-size: 2vh;
  font-weight: bold;
}
.red-btn:focus {
  outline: 2px solid black;
}
.red-btn:hover {
  background-color: rgb(123, 18, 18);
}
.blue-btn {
  background-color: rgb(30, 30, 148);
  width: 10vw;
  height: 5vh;
  border-radius: 1vh;

  border: 0;
  outline: 0;

  color: white;
  font-size: 2vh;
  font-weight: bold;
}
.blue-btn:focus {
  outline: 2px solid black;
}
.blue-btn:hover {
  background-color: rgb(18, 28, 115);
}
</style>
