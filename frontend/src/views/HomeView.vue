<!-- ./frontend/src/views/Home.vue --> 

<template>
    <section>
        <div v-if="isLoggedIn" id="logout">
            <p id="logout">Click <a href="/dashboard">to view all notes</a> </p>
        </div>
        <p v-else>
            <span><a href="/register">register</a></span>
            <span> or </span>
            <span><a href="/login">Login</a></span>
        </p>
    </section>
</template>

<script>

export default {
    name: "HomeVue",
    computed: {
        isLoggedIn: function() {
            return this.$store.getters.isAuth;
        }
    }
}

</script>