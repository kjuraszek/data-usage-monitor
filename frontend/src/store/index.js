import Vue from 'vue'
import Vuex from 'vuex'
import Vuetify from '@/plugins/vuetify'

Vue.use(Vuex)

export const store = new Vuex.Store({
    state: {
        loading: true,
        darkMode: localStorage.getItem('darkMode') === 'true',
      },
    mutations: {
        switchLoading (state) {
            state.loading = !state.loading
        },
        switchDarkMode (state) {
            state.darkMode = !state.darkMode
            Vuetify.framework.theme.dark = state.darkMode
        }
    }
})