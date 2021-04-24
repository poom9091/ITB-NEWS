<template lang="">
  <div v-if="user.name" class="p-4 flex flex-col space-y-2">
    <div>
      Comment as <b class="text-blue-500">{{ user.name }}</b>
    </div>
    <div class="-y-0 flex-col flex">
      <textarea
        v-model="comment"
        placeholder="What are your thoughts"
        rows="3"
        id="title"
        class=" w-full border-2 text-black p-2  "
      />
      <div class=" bg-blue-100 p-2 py-1 text-right ">
        <button
          v-if="!comment"
          class="p-1 px-4 bg-gray-400 rounded-full text-white max-w-max"
        >
          Comment
        </button>
        <button
          v-else
          v-on:click="setComment()"
          class="p-1 px-4 bg-gray-800 rounded-full text-white hover:bg-gray-600 "
        >
          Comment
        </button>
      </div>
    </div>
  </div>
  <div v-else class="text-center py-4 space-y-2">
    <div class="italic">You can not comment plase Login</div>
    <button
      v-on:click="this.$router.push('/login')"
      class="text-white px-3 py-1 bg-blue-500 rounded-md italic"
    >
      Login to start
    </button>
  </div>
</template>
<script>
import axios from "axios";
import { mapGetters } from "vuex";
export default {
  props: ["post_id"],
  data() {
    return {
      comment: "",
    };
  },
  user: {},
  methods: {
    ...mapGetters(["getUID"]),

    setComment() {
      let THtime = new Date().toLocaleString("th-TH", {
        year: "numeric",
        month: "numeric",
        day: "numeric",
        hour: "2-digit",
        minute: "2-digit",
      });
      let commentdata = {
        user_id: this.user.uid,
        username: this.user.name,
        desc: this.comment,
        post_id: this.post_id,
        time: THtime,
      };
      console.log(commentdata);

      axios.post("http://127.0.0.1:5000/createcomment", commentdata);
      this.$router.go(this.$router.currentRoute);
      this.$forceUpdate();

      // .then((response) => (console.log(response.data)));
    },
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
