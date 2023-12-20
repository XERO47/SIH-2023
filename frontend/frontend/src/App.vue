<template>
  <div id="app">
    <NavBar />

    <router-view />
  </div>
</template>

<script lang="ts">
import NavBar from '@/components/NavBar.vue';
// import router from './router';

export default {
  name: 'App',
  components: {
    NavBar,
    // router,
  }
};
</script>


