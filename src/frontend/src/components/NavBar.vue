<!-- ./frontend/src/components/NavBar.vue -->

<template>
  <header>
    <nav class="navbar navbar-expand-md navbar-dark bg-dark">
      <div class="container">
        <a class="navbar-brand" href="/">Web Notepad</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse"
          aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle Nav">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarCollapse">
          <ul v-if="isLoggedIn" class="navbar-nav me-auto mb-2 mb-md-0">
            <li class="nav-item">
              <router-link class="nav-link" to="/">Главная</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/dashboard">Панель управления</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/profile">Мой профиль</router-link>
            </li>
            <li class="nav-item">
              <a class="nav-link" @click="logout">Выйти</a>
            </li>
          </ul>
          <ul v-else class="navbar-nav me-auto mb-2 mb-md-0">
            <li class="nav-item">
              <router-link class="nav-link" to="/">Главная</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/register">Регистрация</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/login">Войти</router-link>
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
    isLoggedIn: function () {
      return this.$store.getters.isAuth;
    }
  },
  methods: {
    async logout() {
      await this.$store.dispatch('logout');
      this.$router.push('login');
    }
  }
}

</script>

<style scoped>
a {
  cursor: pointer;
}
</style>