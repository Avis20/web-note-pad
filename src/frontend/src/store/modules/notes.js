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
        let {data} = await axios.post('api/v1/note/list', {})
        commit('setNotes', data.list)
    },
};

const mutations = {
    setNotes(state, notes) {
        state.notes = notes;
    }
}

export default {
    state,
    getters,
    actions,
    mutations
};

