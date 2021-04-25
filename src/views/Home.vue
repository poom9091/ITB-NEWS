<template>
  <div class=" h-screen">
    <title_ITB class=""/>
    <title_news />
    <title_post />
  </div>
</template>

<script>
// @ is an alias to /src
import title_post from '../components/title_post.vue'
import title_news from '../components/title_news.vue'
import title_ITB from '../components/title.vue' 
export default {
  name: 'Home',
  loadtest:"",
  components: {
    title_ITB,
    title_news,
    title_post
  },


}
</script>
