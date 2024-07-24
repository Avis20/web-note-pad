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
        console.log(data);
        commit('setNote', data.item)
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

