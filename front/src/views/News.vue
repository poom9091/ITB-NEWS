<template>
  <div class="  h-screen">
    <div class=" h-2/6 bg-blue-500 flex  mt-8 shadow-lg ">
      <div
        class=" text-3xl  sm:text-5xl text-white font-black m-auto font-sans  "
      >
        Recommend News
      </div>
    </div>
    <all_new
      class="px-3 sm:w-10/12 m-auto rounded-md -mt-16 bg-white shadow-2xl z-0 "
    />
  </div>
</template>

<script>
import all_new from "../components/all_new.vue";

export default {
  news: [],
  data() {
    return {};
  },
  components: {
    all_new,
  },
  created() {
    this.news = this.$store.getters.getNews;
    // console.log(this.news);
  },
};
</script>
