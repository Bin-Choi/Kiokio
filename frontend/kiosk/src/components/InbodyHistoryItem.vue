<template>
  <div
    @click="goDetail()"
    class="row rounded"
    style="margin: 1vh 0; font-size: 1.5vh"
  >
    <p class="col">{{ date[0].slice(-2) }}/{{ date[1] }}/{{ date[2] }}</p>
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
        method: 'get',
        url: `${this.axios_URL}/students/inbody/${this.inbody.pk}/`,
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
  border: 0.2vh solid #2b64aa2d;
  box-shadow: 0.1vh 0.1vh 0.1vh #2b64aa1e;
}
</style>
