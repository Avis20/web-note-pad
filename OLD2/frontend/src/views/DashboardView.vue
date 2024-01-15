
<template>
    <div>
        <section>
            <h3>Добавить новую заметку</h3>
            <hr><br>
            
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
        
        <br><br>

        <h3>Заметки</h3>
        <hr><br>
        <div v-if="notes.length">
            <div v-for="note in notes" :key="note.id">
            <div class="card">
                <div class="card-body">
                    <ul>
                        <li><b>Заметка:</b> {{ note.title }}</li>
                        <li><b>Автор:</b> {{ note.id }}</li>
                        <li><router-link :to="{name: 'Note', params:{id: note.id}}">Подробнее</router-link></li>
                    </ul>
                </div>
            </div>
        </div>
            
        </div>

    </div>
</template>

<style>
.card {
    margin-right: 20px;
    width: 20rem;
    float: left;
}
.card ul li {
    text-align: left;
}
/*
.card ul li {
    list-style-type: none;
}
*/
</style>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
    name: 'DashboardVue',
    data() {
        return {
            form: {
                title: '',
                content: ''
            }
        }
    },
    created: function() {
        return this.$store.dispatch('note_list')
    },
    computed: {
        ...mapGetters({ notes: 'stateNotes' })
    },
    methods: {
        ...mapActions(['note_add']),
        async submit() {
            console.log(this.form);
            await this.note_add(this.form)
        }
    }
}

</script>