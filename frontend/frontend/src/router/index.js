import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  { path: '/', redirect: '/login', component: () => import('@/views/LogIn.vue') },
  { path: '/login', component: () => import('@/views/LogIn.vue') },
  { path: '/home', component: () => import('@/views/Home.vue') },
  { path: '/dashboard/:sbom_id', component: () => import('@/views/Dashboard.vue') },
  { path: '/:notFound(.*)', component: () => import('@/views/notFound.vue') },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
