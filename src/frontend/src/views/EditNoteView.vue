<template>
    <section>
        <h1>Редактировать заметку</h1>
        <hr /><br />


        <form @submit.prevent="submit">
            <div class="mb-3">
                <label for="title" class="form-label">Заголовок</label>
                <input type="text" name="title" v-model="form.title" class="form-control">
            </div>
            <div class="mb-3">
                <label for="content" class="form-label">Содержание</label>
                <textarea name="content" v-model="form.content" class="form-control"></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Отправить</button>
        </form>
    </section>
</template>

<script>

import { mapActions, mapGetters } from 'vuex'

export default {
    name: 'EditNoteVue',
    props: ['id'],

    data() {
        return {
            form: {
                title: '',
                content: '',
            }
        }
    },

    created: function () {
        this.GetNote();
    },
    computed: {
        ...mapGetters({ note: 'stateNote' })
    },
    methods: {
        ...mapActions(['updateNote', 'getNote']),
        async GetNote() {
            try {
                await this.getNote(this.id);
                this.form.title = this.note.title;
                this.form.content = this.note.content;
            } catch (error) {
                console.log(error);
                this.$router.push('/dashboard');
            }
        },
        async submit() {
            try {
                let note = {
                    id: this.id,
                    form: this.form,
                };
                await this.updateNote(note);
                this.$router.push({ name: 'Note', params: { id: this.note.id } });
            } catch (error) {
                console.log(error);
            }
        },
    },

};
</script>
