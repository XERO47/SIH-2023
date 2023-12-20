<template>
    <div class="container">
        <table class="table">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Date</th>
                    <th>Time</th>
                    <th>Created by</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="sbomList in sbomlist" :key="sbomList.sbom_id">
                    <td>SBOM/{{ formatDate(sbomList.date) }}</td>
                    <td>{{ formatDate(sbomList.date) }}</td>
                    <td>{{ formatTime(sbomList.date) }}</td>
                    <td>admin1</td>
                    <td><button @click="dashboard(sbomList.sbom_id)">view</button></td>
                </tr>
            </tbody>
        </table>
        <div v-if="sbomlist.length === 0" class="message">
            No SBOMs found.
        </div>
        <!-- Button trigger modal -->
        <button type="button" class="btn btn-dark" data-bs-toggle="modal" data-bs-target="#exampleModal">
            Generate SBOM
        </button>

        <!-- Modal -->
        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="exampleModalLabel">Generate SBOM</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="input-group flex-nowrap">
                            <span class="input-group-text" id="addon-wrapping">@</span>
                            <input type="text" class="form-control" placeholder="Github link" aria-label="Github link"
                                aria-describedby="addon-wrapping" v-model="link" required>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button @click="submit_link" class="btn btn-secondary" data-bs-dismiss="modal">Generate</button>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>

import { mapGetters } from 'vuex';

export default {
    name: 'HomeView',
    data() {
        return {
            link: '',
            sbomlists: [],
            user_id: ''
        }
    },
    methods: {
        submit_link() {
            const payload = {
                repo_link: this.link,
                user_id: this.user_id
            }
            this.$store.dispatch('send_repo_link', payload);
        },
        formatDate(dateTimeString) {
            let dateObject = new Date(dateTimeString);
            return dateObject.toISOString().split('T')[0];
        },
        formatTime(dateTimeString) {
            let dateObject = new Date(dateTimeString);
            return dateObject.toTimeString().split(' ')[0];
        },
        dashboard(sbom_id) {
            this.$router.push(`/dashboard/${sbom_id}`);
        }
    },
    computed: {
        ...mapGetters(['isLogged', 'getRole']),

        sbomlist() {
            return this.$store.state.sbomlist;
        }
    },
    created() {
        const user = this.$store.state.user;
        this.user_id = user ? user.replace(/"/g, '') : null;

    },
    mounted() {
        this.$store.dispatch('fetch_all_sbom');
        this.sbomlists = this.$store.getters.getlist;
    }
}

</script>

<style scoped>
.container {
    display: block;
    min-height: 86vh;
    margin: 0.5rem auto;
    max-width: 97%;
    background-color: #f4efef;
    padding: 5px;
    border-radius: 10px;
}

table {
    border-radius: 10px !important;
}

.message {
    display: flex;
    justify-content: start;
    background-color: azure;
    border-radius: 10px;
    padding: 8px;
    border: 1px solid #c3c3c3;
    margin-top: 0.2rem;
    margin-bottom: 1rem;
}
</style>