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
                <tr v-for="sbomList in sbomlist" :key="sbomList.id">
                    <td>{{ sbomList.name }}</td>
                    <td>{{ sbomList.date }}</td>
                    <td>{{ sbomList.time }}</td>
                    <td>{{ sbomList.createdBy }}</td>
                    <td><a href="">view</a></td>
                </tr>
            </tbody>
        </table>
        <div v-if="sbomlists.length === 0" class="message">
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
    name: 'tableComp',
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
        }
    },
    computed: {
        ...mapGetters(['isLogged', 'getRole','getlist']),

        sbomlist() {
            return this.$store.state.sbomlist;
        }
    },
    created() {
        const user = this.$store.state.user;
        this.user_id = user ? user.replace(/"/g, '') : null;
        this.$store.getters.getlist;
        this.sbomlist = this.$store.getters.getlist;
    }
}
</script>

<style scoped>
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