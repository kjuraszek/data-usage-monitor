import { Home, NotFound, Settings } from '@/views'

export default [
    { path: '/', name: 'home', component: Home },
    { path: '/settings', component: Settings },
    { path: '*', component: NotFound }
]