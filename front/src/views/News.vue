<template>
  <div class="about">
    <Recommend_new class="w-11/12 m-auto my-4" />
  </div>
</template>

<script>

import Recommend_new from '../components/recommend_new.vue'
export default {
  news:[],
  components:{
    Recommend_new
  },
  created(){
    this.news= this.$store.getters.getNews
    // console.log(this.news);
  },
}
</script>