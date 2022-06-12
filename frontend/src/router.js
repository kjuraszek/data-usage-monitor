import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from './components/Home'
import NotFound from './components/NotFound'
import WorkInProgress from './components/WorkInProgress'

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