<template>
    <section>
        <h1>Ваш профиль</h1>
        <hr><br>
        <div>
            <p><strong>Имя:</strong> <span>{{ user.username }}</span></p>
            <p><strong>ФИО:</strong> <span>{{ user.full_name }}</span></p>
            <p><button @click="deleteUser" class="btn btn-danger">Удалить профиль</button></p>
        </div>
    </section>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
    name: 'ProfileView',
    created: function() {
        return this.$store.dispatch('user_info')
    },
    computed: {
        ...mapGetters({ user: 'stateUser' })
    },
    methods: {
        ...mapActions(['delete_user']),
        async deleteUser() {
            console.log('AAAAAAAAa');
            await this.delete_user(this.user.id)
            // try {
            // } catch (error) {
            //     console.error(error);
            // }
        }
    }
}

</script>
