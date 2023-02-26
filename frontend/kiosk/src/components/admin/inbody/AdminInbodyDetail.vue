<template>
  <div class="d-flex flex-column">
    <div
      class="d-flex"
      @click="$emit('change-mode-default')"
      style="font-size: 3vh; cursor: pointer"
    >
      <font-awesome-icon icon="fa-solid fa-circle-arrow-left" />
    </div>
    <div clsss="d-flex" v-if="mode === 'R'">
      <AdminInbodyDetailRead
        :studentIndex="studentIndex"
        :inbodyIndex="inbodyIndex"
        @change-mode-U="mode = 'U'"
        @change-mode-default="$emit('change-mode-default')"
      />
    </div>
    <div v-if="mode === 'U'">
      <AdminInbodyDetailUpdate
        :studentIndex="studentIndex"
        :inbodyIndex="inbodyIndex"
        @change-mode-R="mode = 'R'"
      />
    </div>
  </div>
</template>

<script>
// import AdminInbodyDetailRead from '@/components/admin/inbody/AdminInbodyDetailRead.vue'
// import AdminInbodyDetailUpdate from '@/components/admin/inbody/AdminInbodyDetailUpdate.vue'
import AdminInbodyDetailRead from './AdminInbodyDetailRead.vue'
import AdminInbodyDetailUpdate from './AdminInbodyDetailUpdate.vue'

export default {
  name: 'AdminInbodyDetail',
  components: {
    AdminInbodyDetailRead,
    AdminInbodyDetailUpdate,
  },
  props: {
    studentIndex: Number,
    inbodyIndex: Number,
  },
  data() {
    return {
      mode: 'R',
    }
  },
}
</script>

<style scoped></style>
