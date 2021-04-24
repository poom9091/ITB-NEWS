<template lang="">
  <div class=" mt-14 sm:mt-24  mb-10 md:w-8/12 mx-auto border-gray-500 rounded-md  divide-y ">
    <news :post_id="this._id" class="border-r-2 border-l-2" />
    <createcm :post_id="this._id" />
    <comment :post_id="this._id" />
  </div>
</template>

<script>

import comment from "../components/Commented/comment_CM";
import news from "../components/Commented/comment_New";
import createcm from "../components/Commented/Create_cm"
export default {
  _id: "",
  components: {
    comment,
    news,
    createcm
  },
  created()  {
    this._id = this.$route.params._id;
  },
};
</script>

<style lang=""></style>
