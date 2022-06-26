import Vue from 'vue'
import VueRouter from 'vue-router'
import VueMeta from 'vue-meta'
import { Home, NotFound, WorkInProgress, Settings } from '@/views'

Vue.use(VueRouter)
Vue.use(VueMeta)

export const router = new VueRouter({
    mode: 'history',
    routes: [
        { path: '/', name: 'home', component: Home },
        { path: '/settings', component: Settings },
        { path: '*', component: NotFound }
        ],
})