export default {
    getUser(state) {
        return state.user;
    },
    getRole(state) {
        return state.role;
    },
    getSuccessMsg(state) {
        return state.successMessage;
    },
    getErrorMsg(state) {
        return state.errorMessage;
    },
    isLogged(state) {
        return state.isLogged;
    },

    getlist(state) {
        return state.sbomlist;
    },

    getsbom(state) {
        return state.sbom;
    }
};