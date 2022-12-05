<template>
  <div id="app">
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
  width: 100vw;
  height: 100vh;
  text-align: center;
  background-color: #2b64aa1e;
}

#title{
  box-shadow: 0 7px 7px rgba(17, 61, 147, 0.987); 
}
</style>
