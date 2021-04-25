import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import login from '../views/Login.vue'
import template_login from '../components/login&register/template_login'
import register from '../components/login&register/register.vue'
import Board from '../views/Board.vue'
import all_post_profile from  '../components/Posted/all_post_profile'
import all_post_topic from '../components/Posted/all_post_topic'
import all_post from '../components/Posted/all_post'
import News from '../views/News.vue'
import Createpost from '../views/Createpost.vue'
import Comment from '../views/Comment.vue'
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: login,
    children:[
      {
        path:'',
        component: template_login
      },
      {
        path:'register',
        component: register
      },
    ]
  },
  {
    path: '/board',
    name: 'Board',
    component: Board,
    children:[
      {
        name:'Board_profile',
        path:'profile/:uid/:name',
        component: all_post_profile,
        props:true
      },
      {
        path:'topic_news/:topic',
        component: all_post_topic,
        props:true
      },
      {
        path:'',
        component: all_post
      },
    ]
  },
  {
    path: '/news',
    name: 'News',
    component: News
  },
  {
    path: '/createboard/:title',
    name: 'Create',
    component: Createpost,
    props:true
  },
  {
    path: '/comment/:_id',
    name: 'Comment',
    component: Comment,
    prop:true
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
