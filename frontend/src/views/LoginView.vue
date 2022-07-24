<template>
    <section>
        <form @submit.prevent="submit">
        <div class="mb-3">
            <label for="username" class="form-label">Имя пользователя:</label>
            <input type="text" name="username" v-model="form.username" class="form-control" />
        </div>
        <div class="mb-3">
            <label for="password" class="form-label">Пароль:</label>
            <input type="password" name="password" v-model="form.password" class="form-control" />
        </div>
        <button type="submit" class="btn btn-primary">Войти</button>
        </form>
    </section>
</template>

<script>
import { mapActions } from "vuex";
export default {
    name: 'LoginView',
    data() {
        return {
            form: {
                username: "",
                password: ""
            },
        };
    },
    methods: {
        ...mapActions(['login']),
        async submit() {
            const User = new FormData()
            User.append('username', this.form.username)
            User.append('password', this.form.password)
            await this.login(User);
            this.$router.push('/dashboard');
        }
    }
}
</script>
