
import axios from 'axios'

const state = {
    notes: null,
    note: null
}

const getters = {
    stateNotes: state => state.notes,
    stateNote: state => state.note,
}

const actions = {
    async note_add({dispatch}, note) {
        await axios.post('/api/v1/note/add', note);
        await dispatch('note_list');
    },
    async note_list({commit}) {
        let {data} = await axios.get('/api/v1/note/list')
        commit('setNotes', data)
    },
    async note_get({commit}, id) {
        let {data} = await axios.get(`/api/v1/note/get/${id}`)
        commit('setNote', data)
    },
    // eslint-disable-next-line no-empty-pattern
    async note_delete({}, id) {
        await axios.delete(`/api/v1/note/delete/${id}`)
    }
}

const mutations = {
    setNotes(state, notes) {
        state.notes = notes;
    },
    setNote(state, note) {
        state.note = note
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}
