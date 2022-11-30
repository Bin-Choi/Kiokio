<template>
  <div id="app">
    
    <router-view/>

    <footer style="height: 150px;"
    class="bg-light w-100 fixed-bottom d-flex justify-content-center align-items-center" >
      <img src="#" alt="Logo">
      <span>딩초초등학교</span>
    </footer>
  </div>
</template>

<script>

export default {
  name: 'AppView',
}
</script>

<style>
* {
  font-size: 50px;
}

#app {
  height: 100vh;
  text-align: center;
  background-color: #2b64aa1e;
}
</style>
