<template>
  <div class="modal-bg">
    <div class="modal-content rounded shadow m-auto" style="padding: 2vh">
      <div
        id="title"
        class="w-75 bg-primary rounded text-light shadow m-auto"
        style="font-size: 5vh"
      ></div>

      <!-- ATTEND CONTENT -->
      <span
        v-if="$route.name === 'attend'"
        class="w-75 h-75 m-auto bg-light rounded shadow d-flex flex-column align-items-center justify-content-evenly"
      >
        <div style="font-size: 2.5vh">
          <div>
            {{ student.grade }}학년 {{ student.room }}반 {{ student.number }}번
            {{ student.name }}
          </div>
          <hr />
          <div>
            날짜 | {{ student.date }} <br />
            시간 | {{ student.time.split('.')[0] }}
          </div>
        </div>

        <div class="d-flex flex-column">
          <button type="button" class="btn btn-success shadow" @click="attend">
            출석하기
          </button>
          <button
            type="button"
            class="btn btn-danger shadow"
            @click="$emit('close-modal')"
          >
            취소
          </button>
        </div>
      </span>

      <!-- GYM CONTENT -->
      <span
        v-if="$route.name === 'gym'"
        class="w-75 h-75 bg-light m-auto rounded d-flex flex-column align-items-center justify-content-between shadow"
        style="padding: 2vh"
      >
        <img src="#" alt="IMG" />
        <div>description</div>
        <button
          type="button"
          class="btn btn-primary shadow"
          @click="$emit('close-modal')"
        >
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
  name: 'ModalView',
  props: {
    student: Object,
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
          // close modal
          this.$emit('close-modal')
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  mounted() {
    const title = document.querySelector('.modal-content #title')
    if (this.$route.name == 'gym') {
      title.innerText = '운동기구'
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
  background-color: #e7f1ff;
}

button {
  margin: 1vh;
  font-size: 3vh;
}
</style>
