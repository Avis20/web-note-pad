<!-- ./frontend/src/views/Home.vue --> 

<template>
  <section>
    <div v-if="isLoggedIn" id="logout">
      <p id="logout"><a href="/dashboard">Нажмите</a> чтобы увидеть все заметки</p>
    </div>
    <p v-else>
      <span><a href="/login">Войти</a><hr></span>
      <span>Не получается войти?<hr></span>
      <span><a href="/register">Зарегистрироваться</a></span>
    </p>
  </section>
</template>

<script>

export default {
  name: "HomeVue",
  computed: {
    isLoggedIn: function() {
      console.log('isAuth', this.$store.getters.isAuth);
      return this.$store.getters.isAuth;
    }
  }
}

</script>
