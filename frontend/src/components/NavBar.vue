<!-- ./frontend/src/components/NavBar.vue --> 

<template>
    <header>
        <nav class="navbar navbar-expand-md navbar-dark bg-dark">
            <div class="container">
                <a class="navbar-brand" href="/">Fast API + Vue</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse"
                    aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle Nav">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarCollapse">
                    <ul v-if="isLoggedIn">
                        <li class="nav-item">
                            <route-link class="nav-link" to="/">Home</route-link>
                        </li>
                    </ul>
                    <ul v-else class="navbar-nav me-auto mb-2 mb-md-0">
                        <li class="nav-item">
                            <route-link class="nav-link" to="/">Home</route-link>
                        </li>
                        <li class="nav-item">
                            <route-link class="nav-link" to="/register">Register</route-link>
                        </li>
                        <li class="nav-item">
                            <route-link class="nav-link" to="/login">Login</route-link>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </header>
</template>

<script>

export default {
    name: "NavBar",
    computed: {
        isLoggedIn: function() {
            return this.$store.getters.isAuth;
        }
    }
}

</script>

<style scoped>
a {
    cursor: pointer;
}
</style>