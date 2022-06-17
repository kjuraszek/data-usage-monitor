import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home'
import NotFound from '@/views/NotFound'
import WorkInProgress from '@/views/WorkInProgress'

Vue.use(VueRouter)

export const router = new VueRouter({
    mode: 'history',
    routes: [
        { path: '/', name: 'home', component: Home },
        { path: '/settings', component: WorkInProgress },
        { path: '/help', component: WorkInProgress },
        { path: '*', component: NotFound }
        ],
})