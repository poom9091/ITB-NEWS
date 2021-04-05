<template>
  <div id="nav">
    <Navbar/>
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
  },
  methods:{
    ...mapActions(['getNewsFromApi'])
  }
}
</script>

