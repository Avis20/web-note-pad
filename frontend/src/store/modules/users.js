// ./frontend/src/store/modules/users.js

import axios from "axios";

const state = {
    user: null,
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
        console.log(user);
        await axios.post('login', user);
        await dispatch('user_info');
    },
    async user_info({commit}) {
        let {data} = await axios.get('user/info')
        console.log(data);
        await commit('SetUser', data)
    }
}

export default {
    state,
    actions
}
