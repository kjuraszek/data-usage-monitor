import Vue from 'vue'
import VueRouter from 'vue-router'
import { Home, NotFound, WorkInProgress, Settings } from '@/views'

Vue.use(VueRouter)

export const router = new VueRouter({
    mode: 'history',
    routes: [
        { path: '/', name: 'home', component: Home },
        { path: '/settings', component: Settings },
        { path: '/help', component: WorkInProgress },
        { path: '*', component: NotFound }
        ],
})