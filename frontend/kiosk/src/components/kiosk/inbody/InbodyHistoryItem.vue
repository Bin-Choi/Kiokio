<template>
  <div @click="goDetail" class="w-100 row shadow-sm">
    <p class="col" style="line-height: 4vh">
      {{ date[0].slice(-2) }}/{{ date[1] }}/{{ date[2] }}
    </p>
    <p class="col">{{ inbody.age }} 세</p>
    <p class="col">{{ inbody.height }} cm</p>
    <p class="col">{{ inbody.weight }} kg</p>
    <p class="col">{{ inbody.percent_body_fat }} %</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'inbodyHistoryItem',
  data() {
    return {
      date: this.inbody.test_date.split('-'),
    }
  },
  props: {
    inbody: Object,
  },
  computed: {
    axios_URL() {
      return this.$store.state.axios_URL
    },
  },
  methods: {
    goDetail() {
      axios({
        method: 'post',
        url: `${this.axios_URL}/students/${this.$store.state.student.id}/inbody/${this.inbody.id}/`,
        data: {
          password: this.$store.state.student.password,
        },
      })
        .then((res) => {
          this.$store.commit('INBODY_INFO', res.data)
          this.$router.push({ name: 'inbodyDetail' })
        })

        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style scoped>
div {
  height: 4vh;
  margin: 1vh 0;
  font-size: 1.4vh;
  border-radius: 1vh;
  border: 0.25vh solid #ffa946;
  background-color: #ffe1be48;
}

.col {
  line-height: 4vh;
}
</style>
