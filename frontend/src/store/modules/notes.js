
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
    async createNote({dispatch}, note) {
        await axios.post('note/add', note);
        await dispatch('getNotes');
    },
    async getNotes({commit}) {
        let {data} = await axios.get('note/list')
        commit('setNotes', data)
    },
    async viewNote({commit}, id) {
        let {data} = await axios.get(`note/get/${id}`)
        commit('setNote', data)
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
