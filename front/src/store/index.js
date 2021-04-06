import axios from "axios";
import { createStore } from "vuex";

let urlnew="https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=380094e98a684b578fa885b235439b36"

export default createStore({
  state: {
    news: [],
    isLoading:true
  },
  getters: {
    getNews: (state) => {
      return state.news;
    },
    getLoad: (state) => {
      return state.isLoading;
    }
  },
  mutations: {
    setNews(state, news) {
      state.news = news;
    },
    setLoad(state,load){
      console.log(load);
      state.isLoading=load
    }
  },
  actions: {
    async getNewsFromApi({commit}){
      let n =[]
      await axios.get(urlnew)
      .then((response) => {
        n=response.data.articles
        commit("setNews",response.data.articles)})
        commit("setLoad",false)
      console.log(n)   
    }
  },
  modules: {},
});
