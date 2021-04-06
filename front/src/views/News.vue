<template>
  <div class="about">
    <all_new class="w-11/12 m-auto my-24" />
  </div>
</template>

<script>

import all_new from '../components/all_new.vue'
export default {
  news:[],
  components:{
    all_new
  },
  created(){
    this.news= this.$store.getters.getNews
    // console.log(this.news);
  },
}
</script>