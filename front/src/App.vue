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
    this.getNewsFromApi();
    this.getPostFromApi();
  },
  methods:{
    ...mapActions(['getNewsFromApi','getPostFromApi'])
  }
}
</script>

