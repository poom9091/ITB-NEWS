<template lang="">
  <div class="mt-24 mb-10 w-8/12 mx-auto border-gray-500 rounded-md  divide-y ">
    <news :title="this._id" class="border-r-2 border-l-2" />
    <createcm :title="this._id" />
    <comment :title="this._id" />
  </div>
</template>

<script>
import comment from "../components/comment_CM";
import news from "../components/comment_New";
import createcm from "../components/Create_cm"
export default {
  _id: "",
  components: {
    comment,
    news,
    createcm
  },
  beforeCreate() {
    this._id = this.$route.params._id;
  },
};
</script>

<style lang=""></style>
