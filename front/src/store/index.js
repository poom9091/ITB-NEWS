import axios from "axios";
import { createStore } from "vuex";

let urlnew="https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=380094e98a684b578fa885b235439b36"
let apipost="https://api.jsonbin.io/b/6072cbe55b165e19f61cbc91/1"

export default createStore({
  state: {
    news: [],
    isLoading:true,
    posts:[],
    isLoading_post:true,
    user:{
      uid:'',
      name:''
    }
  },
  getters: {
    getNews: (state) => {
      return state.news;
    },
    getLoad: (state) => {
      return state.isLoading;
    },
    getUID: (state) => {
      return state.user
    }
  },
  mutations: {
    setNews(state, news) {
      state.news = news;
    },
    setLoad(state,load){
      state.isLoading=load
    },
    setPost(state, posts){
      state.posts = posts
    },
    setLoadPost(state,load){
      state.isLoading_post=load
    },
    setUsername(state,user){
      state.user.uid=user.uid
      state.user.name=user.name
    },
  },
  actions: {
    async setUser({commit},user){
      console.log(user.uid);
      console.log(user.name);
      commit('setUsername',user)
    },
    async getNewsFromApi({commit}){
      let n =[]
      await axios.get(urlnew)
      .then((response) => {
        n=response.data.articles
        commit("setNews",response.data.articles)})
        commit("setLoad",false)
      console.log(n)   
    },
    async getPostFromApi({commit}){
      await axios.get(apipost,
        {
          headers:{
            "secret-key":"$2b$10$pJX92cjXZes3hSYfvlbp5e1xRhcBEEUNb3iGF8AAaXms5LFcB6mu2"
          }
        })
      .then((response)=>{
        commit('setPost',response.data)
        commit('setLoadPost',false)
      })
    },
    
  },
  
  modules: {},
});
