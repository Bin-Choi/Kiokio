<template>
  <div class="modal-bg">
    <div class="modal-content m-auto rounded shadow" style="padding: 2vh">
      <font-awesome-icon
        icon="fa-regular fa-circle-xmark"
        class="align-self-end"
        style="font-size: 3.5vh; margin: 0 3vh"
      />

      <div
        id="title"
        class="w-75 bg-primary rounded text-light shadow"
        style="font-size: 4vh; margin: auto; margin-bottom: 2vh; padding: 1vh"
      >
        비밀번호 입력
      </div>

      <!-- PASSWORD INPUT -->
      <div
        class="w-75 h-50 m-auto rounded shadow bg-light d-flex flex-column justify-content-evenly align-items-center"
      >
        <input
          type="password"
          v-model.trim="password"
          maxlength="4"
          minlength="4"
          class="w-50 rounded"
          style="font-size: 3vh; padding: 1vh"
        />

        <button
          type="button"
          class="w-50 btn btn-primary shadow"
          style="font-size: 3vh"
          @click="submit"
        >
          확인
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ModalPwView',
  data() {
    return {
      password: '',
    }
  },
  props: {
    num: String,
  },
  computed: {
    axios_URL() {
      return this.$store.state.axios_URL
    },
    pk() {
      return this.$store.state.studentPk
    },
  },
  methods: {
    // SUBMIT PASSWORD
    submit() {
      // CHECK PASSWORD FORM
      if (!this.password || this.password.length != 4) {
        alert('비밀번호를 정확히 입력해주세요')
        return false
      }

      // Check password
      axios({
        method: 'post',
        url: `${this.axios_URL}/students/${this.num}/inbody/`,
        data: {
          password: this.password,
          pk: this.pk,
        },
      })
        .then((res) => {
          this.$store.commit('INBODY_DETAIL', res.data)
          this.$router.push({ name: 'inbodyDetail' })
        })

        .catch((err) => {
          alert('비밀번호가 틀렸습니다.')
          console.log(err)
        })

      this.password = ''
    },
  },
}
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
