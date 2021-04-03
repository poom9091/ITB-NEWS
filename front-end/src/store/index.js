import axios from 'axios'
import { createStore } from 'vuex'

export default createStore({
  state: {
    news:[]
  },
  getters:{
    getNews:state=>{
      return state.news
    }
  },
  mutations: {
    setNews(state,news){
      state.news=news
    }
  },
  actions: {
    getNewsFromApi(context){
      
      let news
      axios
        .get('https://newsapi.org/v2/top-headlines?country=th&category=technology&apiKey=380094e98a684b578fa885b235439b36')
        .then(response =>{
          // console.log('hi');
          news=response.data
          // console.log(news)
          context.commit('setNews',news)
        })
    }
  },
  modules: {
  }
})
