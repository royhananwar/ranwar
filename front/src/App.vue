<template>
    <div id="app">
        <blog-navbar></blog-navbar>
        <blog-header></blog-header>
        <router-view></router-view>
        <blog-footer></blog-footer>
    </div>
</template>

<script>

import BlogNavbar from './components/Blog/Navbar.vue'
import BlogHeader from './components/Blog/Header.vue'
import BlogFooter from './components/Blog/Footer.vue'

export default {
  name: 'app',
  components: {
      BlogNavbar,
      BlogHeader,
      BlogFooter
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}
</style>
