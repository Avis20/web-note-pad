<template>
    <div v-if="note">
        <p><strong>Заголовок: </strong>{{ note.title }}</p>
        <p><strong>Содержимое: </strong>{{ note.content }}</p>
        <p><strong>Автор: </strong>{{ note.title }}</p>
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
        ...mapGetters({note: 'stateNote', user: 'stateUser'})
    },
    methods: {
        ...mapActions(['getNote'])
    }

}

</script>
