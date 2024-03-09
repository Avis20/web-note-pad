// ./frontend/src/store/index.js

import createPersistentState from "vuex-persistedstate";
import Vue from 'vue';
import Vuex from 'vuex';

import users from "./modules/users";
import notes from "./modules/notes";

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        users,
        notes,
    },
    plugins: [createPersistentState()]
})
