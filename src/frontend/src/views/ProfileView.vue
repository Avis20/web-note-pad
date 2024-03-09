<!-- ./frontend/src/views/ProfileView.vue -->

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
    return this.$store.dispatch('user_get')
  },
  computed: {
    ...mapGetters({ user: 'stateUser' })
  },
  methods: {
    ...mapActions(['delete_user']),
    async deleteUser() {
      try {
        await this.delete_user(this.user.id)
        await this.$router.push('/')
      } catch (error) {
        console.error(error);
      }
    }
  }
}

</script>