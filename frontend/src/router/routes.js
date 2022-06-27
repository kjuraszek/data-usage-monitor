import { Home, NotFound, Settings } from '@/views'

export const routes = [
    { path: '/', name: 'home', component: Home },
    { path: '/settings', component: Settings },
    { path: '*', component: NotFound }
]