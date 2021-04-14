<template>
  <div id="nav">
    <Navbar class="fixed top-0 w-screen z-40"/>
  </div>
  <router-view/>
</template>

<script>
import {mapActions} from 'vuex';
import Navbar from  './components/Navbar';
export default {
  components:{
    Navbar
  },
  created(){
    if (localStorage.uid && localStorage.name){
       let user = {
          uid: "",
          name: "",
        };
        user.uid = localStorage.uid
        user.name = localStorage.name
        this.setUser(user);
     }
    this.getNewsFromApi();
    this.getPostFromApi();
  },
  methods:{
    ...mapActions(['getNewsFromApi','getPostFromApi','setUser']),
  }
}
</script>

