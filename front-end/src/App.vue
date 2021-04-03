<template>
  <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </div>
  <router-view/>
</template>

<style>
</style>

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
