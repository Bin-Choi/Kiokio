<template>
  <div id="app" class="d-flex flex-column">
    <router-view/>
  </div>
</template>

<script>

export default {
  name: 'AppView',
}
</script>

<style>
* {
  font-size: 1.2em;
}

#app {
  height: 100vh;
  text-align: center;
  background-color: #2b64aa1e;
}
</style>
