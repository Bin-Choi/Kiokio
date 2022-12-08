<template>
  <div id="app" class="d-flex flex-column">
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'AppView',
}
</script>

<style>
@import '~ag-grid-community/styles/ag-grid.css';
@import '~ag-grid-community/styles/ag-theme-alpine.css';

#app {
  height: 100vh;
  text-align: center;
  background-color: #2b64aa1e;
}
</style>
