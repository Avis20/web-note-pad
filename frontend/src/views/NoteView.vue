
<template>
    <section>
        <div class="dsa"></div>
    </section>
</template>

<script>

import { mapGetter, mapActions } from 'vuex'

export default {
    name: 'NoteView',
    props: ['id'],
    async created() {
        try {
            await this.viewNote(this.id)
        } catch (error) {
            console.log(error);
        }
    },
    computed: {
        ...mapGetter({ note: 'stateNote' })
    },
    methods: {
        ...mapActions(['viewNote'])
    }
}

</script>
