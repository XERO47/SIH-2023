<template>
  <div class="container">
    <div class="card p-4">
      <h4 class="mb-4" style=" text-align: center;">Login</h4>
      <form @submit.prevent="submitForm">
        <!-- <div class="form-group">
          <label for="username" style="font-size: 18px; ">Username:</label>
          <input type="text" id="username" class="form-control" v-model="username" required>
        </div> -->
        <div class="input-group flex-nowrap mb-3">
          <span class="input-group-text" id="addon-wrapping">@</span>
          <input type="text" class="form-control" placeholder="Username" aria-label="Username"
            aria-describedby="addon-wrapping" v-model="username" required>
        </div>
        <div class="input-group flex-nowrap">
          <span class="input-group-text" id="addon-wrapping">#</span>
          <input type="password" class="form-control" placeholder="Password" aria-label="Password"
            aria-describedby="addon-wrapping" v-model="password" required>
        </div>
        <!-- <div class="form-group">
          <label for="password" style="font-size: 18px; ">Password:</label>
          <input type="password" id="password" class="form-control" v-model="password" required>
        </div> -->


        <div class="but btn-group " role="group">
          <!-- Edit button with confirmation pop-up -->
          <button type="submit" class="btn btn-primary">Login</button>
          <!-- Enable/Disable button with confirmation pop-up -->
          <!-- <router-link class="btn btn-light" to="/register">Sign Up</router-link> -->

        </div>
      </form>
      <div v-if="is_login" class="alert alert-success mt-4" role="alert" style="font-size: 18px;">
        Successfully logged in as {{ name }}!
      </div>
      <div v-if="error" class="alert alert-danger mt-4" role="alert" style="font-size: 18px;">
        {{ error }}
      </div>
    </div>
  </div>
</template>
  
<script>
import { mapGetters } from 'vuex';

export default {
  name: 'signinView',
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    submitForm(event) {
      event.preventDefault();
      const payload = {
        username: this.username,
        password: this.password,
      };
      this.$store.dispatch('login', payload);
      this.username = '';
      this.password = '';
      this.$router.push('/home');
    },

  },
  computed: {
    ...mapGetters('auth', ['isLogged', 'getSuccessMsg', 'getErrorMsg']),
  },

};
</script>
  
<style scoped>
.error {
  color: red;
  margin-top: 10px;
}

.alert {
  margin-top: 10px;
}

.container {
  display: block;
  min-height: 86vh;
  margin: 0.5rem auto;
  max-width: 97%;
  background-color: #f4efef;
  padding: 20px;
  border-radius: 10px;
}

.card {
  max-height: 40%;
  max-width: 22rem;
  margin-left: 25rem;
  margin-top: 3rem;
  border-radius: 10px;

}

.but {
  margin-top: 20px;
  margin-bottom: 10px;
  width: 100%;
  height: 80%;
  font-size: 16px;
  border-radius: 20px;
  transition: 0.3s;
}
</style>
  