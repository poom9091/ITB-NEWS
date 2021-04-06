<template>
  <div>
    Hello
  </div>
</template>

<script>
export default {
  news:[],
  mounted(){
    this.news= this.$store.getters.getNews
    console.log(this.news);
  },
}
</script>

<style>

</style>