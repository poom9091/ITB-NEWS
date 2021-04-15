<template lang="">
  <div class="p-4 flex flex-col space-y-2">
    <div>
      Comment as <b class="text-blue-500">{{ user.name }}</b>
    </div>
    <div class="-y-0 flex-col flex">
        <textarea
        v-model="this.pdes"
        placeholder="What are your thoughts"
        rows="3"
        id="title"
        class=" w-full border-2 text-black p-2  "
        
        />
        <div class=" bg-blue-100 p-2 py-1 text-right ">
            <button class="p-1 px-4 bg-gray-800 rounded-full text-white hover:bg-gray-600 ">Comment</button>
        </div>
    </div>
  </div>
</template>
<script>
import { mapGetters } from "vuex";
export default {
  props: ["title"],
  user: {},
  methods: {
    ...mapGetters(["getUID"]),
  },
  created() {
    this.user = this.getUID();
  },
  mounted() {
    console.log(this.user.name);
  },
};
</script>
<style lang=""></style>
