import { createRouter, createWebHashHistory } from "vue-router";
import HomeView from '../components/Home.vue';
import ServiciosView from '../components/Servicios.vue';
import ContactView from '../components/Contact.vue';

const routes = [
    { path: '/', component: HomeView },
    { path: '/servicios', component: ServiciosView },
    { path: '/contact', component: ContactView }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router


