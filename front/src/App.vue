<template>
  <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </div>
  <router-view/>
</template>

<script>
import {mapActions} from 'vuex';
export default {
  created(){
    this.getNewsFromApi();
  },
  methods:{
    ...mapActions(['getNewsFromApi'])
  }
}
</script>

