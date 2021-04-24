<template>
  <div class=" h-screen w-screen">
    <div class=" h-2/6 bg-blue-500 flex mt-8 shadow-lg ">
      <div class=" m-auto flex space-x-8 items-end"> 
        <div
          class=" text-3xl  sm:text-5xl text-white font-black  font-sans  "
        >
          Board
        </div>
        <sort class=" mx-auto"/>
      </div>
    </div>
    <div class="sm:w-9/12 m-auto rounded-md -mt-16 bg-white shadow-2xl z-0">
      <!-- <div class=" text-4xl font-bold text-blue-500">Board</div> -->
      <router-view class="flex flex-col space-y-2 px-3 py-2" />
    </div>
  </div>
</template>

<script>
// import post from '../components/all_post'
// import post_by_profile from '../components/all_post_profile'
import sort from "../components/sort_post";
import { mapActions } from "vuex";
export default {
  data() {
    return {
      profile: this.$route.params.name,
    };
  },
  mounted() {
    this.getPostFromApi();
    console.log(this.profile);
  },
  methods: {
    ...mapActions(["getPostFromApi"]),
  },
  components: {
    sort,
    // post_by_profile
  },
};
</script>

<style></style>
