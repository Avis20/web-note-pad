<!-- .//frontend/src/views/RegisterView.vue -->

<template>
  <section>
    <form @submit.prevent="submit">
      <div class="mb-3">
        <label for="username" class="form-label">Логин:</label>
        <input type="text" name="username" v-model="user.username" class="form-control" />
      </div>
      <div class="mb-3">
        <label for="full_name" class="form-label">Имя:</label>
        <input type="text" name="full_name" v-model="user.full_name" class="form-control" />
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">Пароль:</label>
        <input type="password" name="password" v-model="user.password" class="form-control" />
      </div>
      <button type="submit" class="btn btn-primary">Отправить</button>
    </form>
  </section>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: 'RegisterView',
  data() {
    return {
      user: {
        username: "",
        full_name: "",
        password: ""
      },
    };
  },
  methods: {
    ...mapActions(['register']),
    async submit() {
      try {
        await this.register(this.user);
        this.$router.push('/dashboard');
      } catch (error) {
        throw 'Имя пользователя уже занято. Пожалуйста, попробуйте еще раз.'
      }
    }
  }
}
</script>
