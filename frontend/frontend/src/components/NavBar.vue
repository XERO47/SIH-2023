<template>
  <nav>
      <router-link class="navbar-brand" to="/" style="font-size: 18px;">SBOM Generator</router-link>
      <div v-if=isLogged>
        <div v-if="user">{{ user }} |
        <a @click="logout" style="font-size: 16px;">Log out</a>
        </div>
        
      </div>
  </nav>
</template>
    
    
  
<script>
import { mapGetters } from 'vuex';

export default {

  name: 'navBar',
  data() {
    return {
    };
  },

  methods: {
    logout() {
      this.$store.dispatch('logout');
      this.$router.push('/login');
    },
  },

  computed: {
    ...mapGetters(['isLogged', 'getRole']),

    user() {
      const user = this.$store.state.user;
      return user ? user.replace(/"/g, '') : null;
    },
  },


};

</script>
  
  
<style scoped>

nav {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem 1rem;
  margin: 0.5rem 1rem;
  border-radius: 10px;
  color: #ffffff;
  cursor: pointer;
  background-color: #141212;
}
</style>