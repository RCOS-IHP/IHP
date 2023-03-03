import { createApp } from 'vue'
import LandingPage from './components/LandingPage/MainPage.vue'
import LoginPage from './components/Login/index.vue'
import { createRouter, createWebHistory } from 'vue-router'

const app = createApp({})

const routes = [
  { path: '/', component: LandingPage },
  { path: '/login', component: LoginPage },
]

const router = createRouter({
  // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
  history: createWebHistory(),
  routes, // short for `routes: routes`
})

app.use(router)
app.mount('#app')
