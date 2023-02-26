<template>
  <div class="modal-bg">
    <div class="modal-content shadow m-auto">
      <div id="title" class="title w-75 shadow m-auto"></div>

      <!-- ATTEND CONTENT -->
      <span
        v-if="$route.name === 'attend'"
        class="w-75 h-75 m-auto bg-white round shadow d-flex flex-column align-items-center justify-content-evenly"
      >
        <span v-if="!attendError">
          <div style="font-size: 2.5vh; margin-bottom: 2vh">
            <div>
              {{ student.grade }}학년 {{ student.room }}반
              {{ student.number }}번
              {{ student.name }}
            </div>
            <hr />
            <div>
              날짜 | {{ student.date }} <br />
              시간 | {{ student.time }}
            </div>
          </div>

          <div class="w-75 d-flex flex-column m-auto">
            <button class="btn btn-success shadow" @click="attend">출석</button>
            <button class="btn btn-danger shadow" @click="$emit('close-modal')">
              취소
            </button>
          </div>
        </span>

        <!-- ATTEND ERROR -->
        <span
          v-if="attendError"
          class="h-100 d-flex flex-column align-items-center justify-content-evenly"
          style="padding: 2vh"
        >
          <div style="color: rgb(193, 32, 42); font-size: 2.6vh">
            이미 출석한 학생입니다.
            <div style="color: black; font-size: 2vh">
              *40분에 한 번 출석 가능합니다.
            </div>
          </div>
          <button class="orange-btn shadow w-50" @click="$emit('close-modal')">
            확인
          </button>
        </span>
      </span>

      <!-- GYM CONTENT -->
      <span
        v-if="$route.name === 'gym'"
        class="w-75 h-75 bg-white m-auto round d-flex flex-column align-items-center justify-content-between shadow"
        style="padding: 2vh"
      >
        <img :src="gymImgSrc" alt="IMG" style="width: 60%" />
        <div>{{ gym.detail }}</div>
        <button class="orange-btn shadow" @click="$emit('close-modal')">
          확인
        </button>
      </span>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const URL = 'http://127.0.0.1:8000'

export default {
  name: 'TheModal',
  data() {
    return {
      attendError: false,
    }
  },
  props: {
    student: Object,
  },
  computed: {
    gym() {
      return this.$store.state.gymContent
    },
    gymImgSrc() {
      return this.gym.photo
    },
  },
  methods: {
    // ATTEND
    attend() {
      axios({
        method: 'post',
        url: `${URL}/students/${this.student.num}/attendance/`,
        data: this.student,
      })
        .then(() => {
          this.$emit('close-modal')
        })
        .catch(() => {
          this.attendError = true
        })
    },
  },
  mounted() {
    const title = document.querySelector('.modal-content #title')
    if (this.$route.name == 'gym') {
      title.innerText = this.gym.title
    } else {
      title.innerText = '출석 확인'
    }
  },
}
</script>

<style scoped>
.modal-bg {
  display: flex;
  align-items: center;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.432);
  position: fixed;
  top: 0;
}

.modal-content {
  width: 80%;
  height: 60%;
  background-color: #ffe8d2;
  padding: 2vh;
}

button {
  border-radius: 2vh;
  margin: 1vh;
  font-size: 3vh;
}
</style>
