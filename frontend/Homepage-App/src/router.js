import { createRouter, createWebHistory } from 'vue-router';
import AboutUsPage from './components/AboutUsPage.vue';

const routes = [
  {
    path: '/aboutus',
    name: 'AboutUsPage',
    component: AboutUsPage,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
