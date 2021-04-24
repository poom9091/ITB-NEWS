import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import(/* webpackChunkName: "about" */ '../views/Login.vue'),
    children:[
      {
        path:'',
        component: () => import('../components/login&register/template_login')
      },
      {
        path:'register',
        component: () => import('../components/login&register/register.vue')
      },
    ]
  },
  {
    path: '/board',
    name: 'Board',
    component: () => import(/* webpackChunkName: "about" */ '../views/Board.vue'),
    children:[
      {
        name:'Board_profile',
        path:'profile/:uid/:name',
        component: () => import(/* webpackChunkName: "about" */ '../components/Posted/all_post_profile'),
        props:true
      },
      {
        path:'topic_news/:topic',
        component: () => import(/* webpackChunkName: "about" */ '../components/Posted/all_post_topic'),
        props:true
      },
      {
        path:'',
        component: () => import('../components/Posted/all_post')
      },
    ]
  },
  {
    path: '/news',
    name: 'News',
    component: () => import(/* webpackChunkName: "about" */ '../views/News.vue')
  },
  {
    path: '/createboard/:title',
    name: 'Create',
    component: () => import(/* webpackChunkName: "about" */ '../views/Createpost.vue'),
    props:true
  },
  {
    path: '/comment/:_id',
    name: 'Comment',
    component: () => import('../views/Comment.vue'),
    prop:true
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
