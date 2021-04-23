<template>
  
  <div v-if="!isLoading_post" class="  ">
  
    
    <div
      v-for="p in posts"
      :key="p.index"
      class=" bg-white rounded-xl border-4 hover:border-black divide-y "
    >
      <template_post class="" :p="p" :user="user" />
    </div>
  </div>
  <div v-else>
    <div>Loading....</div>
  </div>
</template>

<script>

import { mapState, mapGetters, mapActions } from "vuex";
import template_post from "../Posted/template_post";
// import sort_post from "../sort_post"
export default {
  data() {
    return {
      user:{
        uid:null,
        name:null
      },
    };
  },
  components: {
    template_post,
    // sort_post
  },
  computed: {
    ...mapState(["posts", "isLoading_post"]),
  },
  methods: {
    ...mapGetters(["getUID"]),
    ...mapActions(["getPostFromApi"]),
  },
  mounted() {
    this.user = this.getUID();
    console.log(this.posts);
  },
};
</script>

<style></style>
