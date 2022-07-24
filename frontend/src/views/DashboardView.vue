<template>
    <div>
        <section>
            <h1>Добавить новую заметку</h1>
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
    </div>
</template>

<script>
import { mapActions } from 'vuex'

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
    methods: {
        ...mapActions(['createNote']),
        async submit() {
            await this.createNote(this.form)
        }
    }
}

</script>