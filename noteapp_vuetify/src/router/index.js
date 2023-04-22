// Composables
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/Home.vue'
import NoteView from '../views/Note.vue'
import NewNoteView from '../views/NewNote.vue'
import SignUpView from '../views/SignUp.vue'
import LoginView from '../views/Login.vue'

const routes = [
  //{
  //  path: '/',
  //  component: () => import('@/layouts/default/Default.vue'),
  //  children: [
  //    {
  //     path: '',
  //    name: 'Home',
  //      // route level code-splitting
  //      // this generates a separate chunk (about.[hash].js) for this route
  //      // which is lazy-loaded when the route is visited.
  //      component: () => import(/* webpackChunkName: "home" */ '@/views/Home.vue'),
  //    },
  //  ],
  //},
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/sign-up',
    name: 'sign-up',
    component: SignUpView,
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
  },
  {
    path: '/note/:note_id',
    name: 'note',
    component: NoteView,
  },
  {
    path: '/new-note/:note_id',
    name: 'new-note',
    component: NewNoteView,
  },
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
