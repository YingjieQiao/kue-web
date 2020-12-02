<template>
  <div id="app">
    <img src="./assets/kue.jpg">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #141a46;
  margin-top: 60px;
  background-color: #ec8b5e;
  min-height: 100%;
}
</style>
