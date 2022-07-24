// ./frontend/src/store/modules/users.js

import axios from "axios";

const state = {
    user: null,
}

const getters = {
    isAuth: state => !!state.user,
    stateUser: state => state.user,
}

const actions = {
    async register({dispatch}, form) {
        await axios.post('register', form);
        let UserForm = new FormData();
        UserForm.append('username', form.username)
        UserForm.append('password', form.password)
        await dispatch('login', UserForm)
    },
    async login({dispatch}, user) {
        console.log('user', user);
        await axios.post('login', user);
        await dispatch('user_info');
    },
    async user_info({commit}) {
        let {data} = await axios.get('user/info')
        console.log(data);
        await commit('SetUser', data)
    },
    async logout({commit}) {
        let user = null;
        commit('logout', user);
    },
    // eslint-disable-next-line no-empty-pattern
    async delete_user({}, id) {
        console.log('id', id);
        await axios.delete(`user/${id}`)
    }
}

const mutations = {
    SetUser(state, username) {
        state.user = username;
    },
    logout(state, user) {
        console.log('user', user);
        state.user = user;
    }
}

export default {
    state,
    getters,
    mutations,
    actions
}
