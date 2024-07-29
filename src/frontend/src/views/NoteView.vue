<template>
    <div v-if="note">
        <p><strong>Заголовок: </strong>{{ note.title }}</p>
        <p><strong>Содержимое: </strong>{{ note.content }}</p>
        <p><strong>Автор: </strong>{{ note.author.username }}</p>

        <div v-if="user.id === note.author_id">
            <p><router-link :to="{ name: 'EditNote', params: { 'id': note.id } }"
                    class="btn btn-primary">Редактировать</router-link></p>
            <p><button @click="removeNote()" class="btn btn-secondary">Удалить</button></p>
        </div>
    </div>

</template>

<script>

import { mapActions, mapGetters } from 'vuex'

export default {
    name: 'NoteVue',
    props: ['id'],

    async created() {
        await this.getNote(this.id);
    },
    computed: {
        ...mapGetters({ note: 'stateNote', user: 'stateUser' })
    },
    methods: {
        ...mapActions(['getNote', 'deleteNote']),
        async removeNote() {
            try {
                await this.deleteNote(this.id);
                this.$router.push('/dashboard');
            } catch (error) {
                error;
            }
        },
    }

}

</script>
