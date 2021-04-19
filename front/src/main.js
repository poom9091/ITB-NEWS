import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './index.css'
import firebase from 'firebase'
// import VueComp from '@vue/composition-api';


var firebaseConfig = {
    apiKey: "AIzaSyCu3deYnDmHQvl5EgshcgdU6vXVZowTqwU",
    authDomain: "itb-news-66167.firebaseapp.com",
    projectId: "itb-news-66167",
    storageBucket: "itb-news-66167.appspot.com",
    messagingSenderId: "1007126775586",
    appId: "1:1007126775586:web:33edde5eed1b0d2b38477b",
    measurementId: "G-7JND2CJHZ9"
};
firebase.initializeApp(firebaseConfig);

createApp(App).use(store).use(router).mount('#app')
