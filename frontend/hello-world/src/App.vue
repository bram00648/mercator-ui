<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <StatsView />
</template>

<script>
import StatsView from './components/StatsView.vue'

export default {
  name: 'App',
  components: {
    StatsView
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>