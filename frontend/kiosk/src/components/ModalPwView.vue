<template>
  <div class="modal-bg">
    <div class="modal-content m-auto rounded shadow py-5">
      <div
        id="title"
        class="w-75 m-auto bg-primary rounded text-light p-1 shadow"
        style="font-size: 2em"
      >
        비밀번호 입력
      </div>

      <!-- PASSWORD INPUT -->
      <div
        class="w-75 h-75 py-5 m-auto rounded shadow bg-light d-flex flex-column justify-content-evenly align-items-center"
      >
        <input
          type="password"
          v-model.trim="password"
          maxlength="4"
          minlength="4"
          class="w-50 rounded p-3"
          style="font-size: 1.5em"
        />

        <button
          type="button"
          class="w-50 btn btn-primary btn-sm shadow"
          style="font-size: 1.5em"
          @click="submit"
        >
          확인
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ModalPwView',
  data() {
    return {
      password: '',
    };
  },
  props: {
    num: String,
  },
  computed: {
    axios_URL() {
      return this.$store.state.axios_URL;
    },
  },
  methods: {
    // SUBMIT PASSWORD
    submit() {
      // CHECK PASSWORD FORM
      if (!this.password || this.password.length != 4) {
        alert('비밀번호를 정확히 입력해주세요');
        return false;
      }

      // Check password
      axios({
        method: 'post',
        url: `${this.axios_URL}/students/${this.num}/inbody/`,
        data: {
          password: this.password,
        },
      })
        .then(() => {
          console.log('success');
        })

        .catch((err) => {
          alert('비밀번호가 틀렸습니다.');
          console.log(err);
        });

      this.password = '';
    },
  },
};
</script>

<style scoped>
.modal-bg {
  display: flex;
  align-items: center;
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
}

.modal-content {
  width: 90%;
  height: 50%;
  bottom: 20%;
}

input {
  background-color: #2b64aa1e;
}
</style>
