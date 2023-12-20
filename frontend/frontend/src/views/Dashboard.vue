<template>
    <div class="container">
        <h3>Generated SBOM</h3>
        <!-- <div class="cards">
            <div class="cs">
                <p>Sbom name</p>
            </div>
            <div class="cs">
                <p>Date & Time</p>
            </div>
            <div class="cs">
                <p>Components</p>
            </div>
        </div> -->
        <div class="container2">
            <div>
                {{sbom }}
            </div>
        </div>

        <div class="dropdown">
            <a class="btn btn-secondary btn-sm dropstart dropdown-toggle" href="#" role="button" id="dropdownMenuLink"
                data-bs-toggle="dropdown" aria-expanded="false">
                Download
            </a>

            <ul class="dropdown-menu" aria-labelledby="dropdownMenuLink">
                <li><a class="dropdown-item" @click="downloadtech">Technical</a></li>
                <li><a class="dropdown-item" @click="downloadnontech">Non-technical</a></li>

            </ul>
        </div>

    </div>
</template>


<style scoped>
.container {
    display: block;
    justify-content: space-between;
    align-items: center;
    min-height: 86vh;
    margin: 0.5rem auto;
    margin-bottom: 1rem;
    max-width: 97%;
    background-color: #f4efef;
    padding: 20px;
    border-radius: 10px;
}

.cards {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding: 0.5rem 1rem;
    margin: 0.5rem 1rem;
    border-radius: 10px;
    color: #ffffff;
    cursor: pointer;
    background-color: #0c0c0c;
}

.container2 {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding: 0.5rem 1rem;
    margin: 0.5rem 1rem;
    border-radius: 10px;
    color: #ffffff;
    cursor: pointer;
    background-color: #656363;
}

.dropdown {
    display: flex;
    justify-content: flex-end;
    margin-right: 1rem;
}

.dropdown-item{
    cursor: pointer;
}
</style>
        



<script>

export default {
    data() {
        return {
            sbom: [],
        };
    },

    name: 'DashBoard',
    methods: {
        downloadtech() {
            const payload  = {
                sbom_id : "1"
            };
            this.$store.dispatch('download_tech', payload);
        },
        downloadnontech() {
            this.$store.dispatch('download_non_tech');
        },
    },

    mounted() {
        const sbom_id = this.$route.params.sbom_id;
        const payload = {
            sbom_id: sbom_id
        }
        this.$store.dispatch('fetch_by_id', payload);
        this.sbom = this.$store.getters.getsbom;
    }
}
</script>

