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
        await dispatch('LogIn', UserForm)
    }
}

export default {
    state,
    actions
}
