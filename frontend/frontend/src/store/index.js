import Vue from 'vue'
import Vuex from 'vuex'

import mutations from './mutations.js';
import actions from './actions.js';
import getters from './getters.js';

Vue.use(Vuex)

export default new Vuex.Store({
  state() {
    let user = null;
    let role = null;
    try {
      user = JSON.parse(sessionStorage.getItem('user'));
      role = sessionStorage.getItem('role');
    } catch (error) {
      console.error(error);
    }
    return {
      user: user,
      errorMessage: null,
      successMessage: null,
      role: role,
      isLogged: !!user,
      sbomlist: [],
      sbom:[]
    }
  },
  mutations,
  actions,
  getters
})
