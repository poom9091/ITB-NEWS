import axios from "axios";
import { createStore } from "vuex";

let urlnew =
  "https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=380094e98a684b578fa885b235439b36";

// Get all post

let apipost = "http://127.0.0.1:5000/allpost";

export default createStore({
  state: {
    news: [],
    isLoading: true,
    posts: [],
    isLoading_post: true,
    user: {
      uid: null,
      name: null,
    },
  },
  getters: {
    getNews: (state) => {
      return state.news;
    },
    getLoad: (state) => {
      return state.isLoading;
    },
    getUID: (state) => {
      return state.user;
    },
  },
  mutations: {
    setNews(state, news) {
      state.news = news;
    },
    setLoad(state, load) {
      state.isLoading = load;
    },
    setPost(state, posts) {
      state.posts = posts;
    },
    setLoadPost(state, load) {
      state.isLoading_post = load;
    },
    setUsername(state, user) {
      state.user.uid = user.uid;
      state.user.name = user.name;
      console.log(state.user.uid);
      console.log(state.user.name);
    },
    setUserOut(state) {
      state.user.uid = null;
      state.user.name = null;
      console.log(state.user.uid);
      console.log(state.user.name);
    },
    set_sort_post_view(state) {
      state.posts.sort(function(a, b) {
        return b.view - a.view;
      });
    },
    set_sort_post_vote(state) {
      state.posts.sort(function(a, b) {
        return b.view.length - a.view.length;
      });
    },
    set_sort_post_comment(state) {
      state.posts.sort(function(a, b) {
        return b.comment.length - a.comment.length;
      });
    },
  },
  actions: {
    Sort_View({ commit }) {
      commit("set_sort_post_view");
    },
    Sort_Vote({ commit }) {
      commit("set_sort_post_vote");
    },
    Sort_Comment({ commit }) {
      commit("set_sort_post_comment");
    },
    async setUser({ commit }, user) {
      // console.log(user.uid);
      // console.log(user.name);
      commit("setUsername", user);
    },
    Logout({ commit }) {
      commit("setUserOut");
    },

    async getNewsFromApi({ commit }) {
      let n = [];
      await axios.get(urlnew).then((response) => {
        n = response.data.articles;
        commit("setNews", response.data.articles);
      });
      commit("setLoad", false);
      console.log(n);
    },

    // ใช้
    async getPostFromApi({ commit }) {
      // ของ เว็บ
      await axios
        .get(apipost, {
          headers: {
            "secret-key":
              "$2b$10$pJX92cjXZes3hSYfvlbp5e1xRhcBEEUNb3iGF8AAaXms5LFcB6mu2",
          },
        })
        // ของเราเอง
        // await axios.get(apipost)
        .then((response) => {
          commit("setPost", response.data);
          commit("setLoadPost", false);
        });

      // // ใช้
      // async getPostFromApi({ commit }) {
      //   await axios.get(apipost).then((response) => {
      //     commit("setPost", response.data);
      //     commit("setLoadPost", false);
      //   });
    },
  },

  modules: {},
});
