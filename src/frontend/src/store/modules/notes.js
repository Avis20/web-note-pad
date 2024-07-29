import axios from "axios"

const state = {
    notes: null,
    note: null,
};

const getters = {
    stateNotes: state => state.notes,
    stateNote: state => state.note,
};

const actions = {
    async createNote({ dispatch }, note) {
        await axios.post('api/v1/note/add', note);
        await dispatch('getNotes');
    },
    async getNotes({ commit }) {
        let { data } = await axios.post('api/v1/note/list', {})
        commit('setNotes', data.list)
    },
    async getNote({ commit }, note_id) {
        let { data } = await axios.get(`api/v1/note/${note_id}/get`)
        commit('setNote', data.item)
    },
    // eslint-disable-next-line no-empty-pattern
    async deleteNote({}, note_id) {
        await axios.delete(`api/v1/note/${note_id}/delete`)
    },
    // eslint-disable-next-line no-empty-pattern
    async updateNote({}, note) {
        console.log('note_id', note.id);
        console.log('note', note.form);
        await axios.post(`api/v1/note/${note.id}/update`, note.form)
    }
};

const mutations = {
    setNotes(state, notes) {
        state.notes = notes;
    },
    setNote(state, note) {
        console.log(state.note);
        state.note = note;
    }
}

export default {
    state,
    getters,
    actions,
    mutations
};

