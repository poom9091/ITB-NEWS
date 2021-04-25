<template>
  <div v-if="!isLoading_post" class=" ">
    <div
      class="bg-white w-full h-12 rounded-md p-3 flex flex-wrap content-center space-x-3 "
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-8 w-8 text-blue-900"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M5.121 17.804A13.937 13.937 0 0112 16c2.5 0 4.847.655 6.879 1.804M15 10a3 3 0 11-6 0 3 3 0 016 0zm6 2a9 9 0 11-18 0 9 9 0 0118 0z"
        />
      </svg>
      <div class=" font-semibold align-middle my-auto">
        Profile : {{ name }}
      </div>
    </div>

    <div v-for="p in posts" :key="p.index">
      <div
        v-if="p.user_id === uid"
        class=" bg-white rounded-xl border-4 hover:border-black flex-col flex divide-y  "
      >
        <template_post class="" :p="p" :user="user" />
      </div>
    </div>
  </div>
  <div v-else>
    <div>Loading....</div>
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions } from "vuex";
import template_post from "../Posted/template_post";
export default {
  props: ["uid", "name"],
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
    // console.log(this.posts);
    console.log(this.uid);
  },
};
</script>

<style></style>
