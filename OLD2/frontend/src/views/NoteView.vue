
<template>
    <section>
        <div v-if="note">
            <p><b>Заголовок:</b> {{ note.title }}</p>
            <p><b>Содержание:</b> {{ note.content }}</p>
            <p><b>Автор:</b> {{ note.id }}</p>
        </div>

        <div v-if="user.id == note.author_id">
            <p><button @click="deleteNote" class="btn btn-danger">Удалить заметку</button></p>
        </div>
    </section>
</template>

<script>

import { mapGetters, mapActions } from 'vuex'

export default {
    name: 'NoteView',
    props: ['id'],
    async created() {
        try {
            await this.note_get(this.id)
        } catch (error) {
            console.log(error);
        }
    },
    computed: {
        ...mapGetters({ note: 'stateNote', user: 'stateUser' })
    },
    methods: {
        ...mapActions(['note_get', 'note_delete']),
        async deleteNote() {
            try {
                await this.note_delete(this.note.id)
                this.$router.push('/dashboard')
            } catch (error) {
                console.log(error);
            }
        }
    }
}

</script>
