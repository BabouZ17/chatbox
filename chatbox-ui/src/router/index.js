import { createRouter, createWebHistory } from 'vue-router'
import SelectUsername from '../components/SelectUsername.vue'
import Chat from '../components/Chat.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: SelectUsername
    },
    {
      path: '/chat',
      name: 'chat',
      component: Chat
    }
  ]
})

export default router
