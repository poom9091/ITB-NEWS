<template>
  <div class="about">
    <h1 class=" bg-green-200 border-gray-700 border-4">This is an about page</h1>
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