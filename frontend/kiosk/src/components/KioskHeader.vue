<template>
  <div
    class="d-flex justify-content-between"
    style="font-size: 4vh; margin: 3vh; margin-bottom: 0"
  >
    <font-awesome-icon
      icon="fa-solid fa-circle-arrow-left"
      @click="$router.go(-1)"
    />
    <font-awesome-icon
      icon="fa-solid fa-house"
      @click="$router.push({ name: 'index' })"
    />
  </div>
</template>

<script>
export default {
  name: 'kioskHeader',
}
</script>

<style></style>
