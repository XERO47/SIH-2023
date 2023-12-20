import api from '@/services/api';
// import router from '@/router';

export default {

    async login(context, payload) {
        try {
            const response = await api.post('/login', {
                'username': payload.username,
                'password': payload.password
            }
            );

            context.commit('clearMessage');

            if (response.status == 200) {
                context.commit('setUser', response.data.user);
                context.commit('setSuccess', response.data);
                context.commit('setRole', response.data.role);
                // Save the access token in session storage
                sessionStorage.setItem('access_token', response.data.access_token);


            }
        }
        catch (error) {
            context.commit('setError', error);
        }
    },



    async logout(context) {
        if (context.state.isLogged) {
            try {
                const response = await api.post('/logout');

                context.commit('clearMessage');

                if (response.status == 200) {
                    context.commit('unsetUser');
                    context.commit('setSuccess', response.data);
                    sessionStorage.removeItem('access_token');
                    sessionStorage.removeItem('role');
                    sessionStorage.removeItem('user');
                }
            }
            catch (error) {
                context.commit('setError', error);
            }
        }
    },

    async send_repo_link(context, payload) {
        try {
            const response = await api.post('/process_link', {
                'link': payload.repo_link,
            }
            );

            context.commit('clearMessage');

            if (response.status == 200) {
                context.commit('setSuccess', response.data);
                context.commit('setlist', response.data);

            }
        }
        catch (error) {
            context.commit('setError', error);
        }
    },

    async fetch_all_sbom(context) {
        try {
            const response = await api.get('/fetch_all_sbom' );

            context.commit('clearMessage');

            if (response.status == 200) {
                context.commit('setSuccess', response.data);
                context.commit('setlist', response.data);

            }
        }
        catch (error) {
            context.commit('setError', error);
        }
    },

    async fetch_by_id(context, payload) {
        try {
            const response = await api.post('/fetch_by_id', {
                'sbom_id': payload.sbom_id
            }
            );

            context.commit('clearMessage');

            if (response.status == 200) {
                context.commit('setSuccess', response.data);
                context.commit('setSbom', response.data);

            }
        }
        catch (error) {
            context.commit('setError', error);
        }
    },

    async download_tech(context, payload) {
        try {
            const response = await api.post('/download_technical', {
                'sbom_id': payload.sbom_id
            }
            );

            context.commit('clearMessage');

            if (response.status == 200) {
                context.commit('setSuccess', response.data);

            }
        }
        catch (error) {
            context.commit('setError', error);
        }
    },

    async download_non_tech(context, payload) {
        try {
            const response = await api.post('/download_non_tech', {
                'sbom_id': payload.sbom_id
            }
            );

            context.commit('clearMessage');

            if (response.status == 200) {
                context.commit('setSuccess', response.data);

            }
        }
        catch (error) {
            context.commit('setError', error);
        }
    },

}