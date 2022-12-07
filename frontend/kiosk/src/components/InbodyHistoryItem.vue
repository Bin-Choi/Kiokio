<template>
  <div @click="goDetail()" class="row rounded" style="margin: 1vh 0">
    <p class="col">{{ inbody.test_date }}</p>
    <p class="col">{{ inbody.age }}</p>
    <p class="col">{{ inbody.height }}</p>
    <p class="col">{{ inbody.weight }}</p>
    <p class="col">{{ inbody.percent_body_fat }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'inbodyHistoryItem',
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
          this.$store.commit('INBODY_DETAIL', res.data)
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
  border: 0.2vh solid #2b64aa1e;
  box-shadow: 0.1vh 0.1vh 0.1vh #2b64aa1e;
}
</style>
