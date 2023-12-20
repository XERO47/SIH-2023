export default {

    setUser(state, user) {
        state.user = user;
        state.isLogged = !!user;
        sessionStorage.setItem('user', JSON.stringify(user));

    },

    unsetUser(state) {
        state.user = null;
        state.isLogged = false;
        sessionStorage.removeItem('user');

    },

    setRole(state, role) {
        state.role = role;
        sessionStorage.setItem('role', role);
    },

    setError(state, msg) {
        state.errorMessage = msg;
    },

    setSuccess(state, payload) {
        state.successMessage = payload.msg;
    },

    clearMessage(state) {
        state.errorMessage = null;
        state.successMessage = null;
    },

    setlist(state, payload) {
        state.sbomlist = payload;
    },

    setSbom(state, payload) {
        state.sbom = payload;
    },

}
