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
    async register({ dispatch }, form) {
        await axios.post('api/v1/user/registration', form);
        let user_login = {
            'username': form.username,
            'password': form.password,
        };
        await dispatch('login', user_login);
    },
    async login({ dispatch }, user) {
        await axios.post('api/v1/user/login', user);
        await dispatch('user_get');
    },
    async user_get({ commit }) {
        let { data } = await axios.get('api/v1/user/get')
        await commit('SetUser', data.item);
    },
    async logout({ commit }) {
        let user = null;
        commit('logout', user);
    },
    async delete_user({ dispatch }) {
        await axios.delete('api/v1/user/delete');
        await dispatch('logout');
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
