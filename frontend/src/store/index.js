import Vue from 'vue'
import Vuex from 'vuex'
import Vuetify from '@/plugins/vuetify'

Vue.use(Vuex)

export const store = new Vuex.Store({
    state: {
        loading: true,
        darkMode: localStorage.getItem('darkMode') === 'true',
        currentMonthDownload: 0.0,
        currentMonthUpload: 0.0,
        currentTimeStamp: null,
      },
    mutations: {
        switchLoading (state) {
            state.loading = !state.loading
        },
        switchDarkMode (state) {
            state.darkMode = !state.darkMode
            Vuetify.framework.theme.dark = state.darkMode
        },
        changeCurrentMonthDownload (state, value) {
            state.currentMonthDownload = value
        },
        changeCurrentMonthUpload (state, value) {
            state.currentMonthUpload = value
        },
        changeCurrentTimeStamp (state, value) {
            state.currentTimeStamp = value
        },
        updateUsageData (state, payload) {
            state.currentMonthDownload = payload.currentMonthDownload
            state.currentMonthUpload = payload.currentMonthUpload
            state.currentTimeStamp = payload.currentTimeStamp
        }
    }
})