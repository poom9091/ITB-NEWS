<template lang="">
  <div class="mt-24 w-8/12 mx-auto">
    <news :title="this._id" />
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
