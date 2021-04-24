<template lang="">
  <div class="p-4 flex-col flex space-y-4">
    <div
      v-for="comment in comments"
      :key="comment.index"
      class=" border-l-2 border-t-2 py-2 space-y-1"
    >
      <div class="flex flex-row justify-between">
        <div class=" flex space-x-2 items-end px-3">
          <div class=" text-base font-medium">{{ comment.username }}</div>
          <div class=" text-xs text-gray-500 italic font-light">
            {{ comment.time }}
          </div>
        </div>
        <div v-if="comment.user_id === user.uid" class="flex space-x-2 px-2 ">
          <button
            class="text-gray-400 hover:text-gray-800"
            v-on:click="geteditComment(comment._id)"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z"
              />
            </svg>
          </button>
          <button
            class="text-gray-400 hover:text-gray-800"
            v-on:click="delComment(comment)"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                fill-rule="evenodd"
                d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z"
                clip-rule="evenodd"
              />
            </svg>
          </button>
        </div>
      </div>
      <div v-if="edit && comment_id_edit === comment._id" class="px-5">
        <textarea
          v-model="comment.desc"
          class="px-2 py-1 border-2 border-dashed border-gray-300 w-full"
          rows="2"
        />
        <div class="space-x-2 text-right">
          <button
            class="p-1 px-3 text-white rounded-md bg-blue-500 hover:bg-blue-800"
            v-on:click="editComment(comment)"
          >
            Save
          </button>
          <button
            class="p-1 px-3 text-white rounded-md bg-gray-500 hover:bg-gray-800"
            v-on:click="this.edit = false"
          >
            Cancel
          </button>
        </div>
      </div>
      <div v-else class="px-5">
        {{ comment.desc }}
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import { mapGetters } from "vuex";
export default {
  data() {
    return {
      edit: false,
      comment_id_edit: "",
      comments: [],
      user: {
        uid: "",
        name: "",
      },
    };
  },
  props: ["post_id"],
  isLoad: false,
  methods: {
    ...mapGetters(["getUID"]),

    geteditComment(id) {
      this.edit = true;
      this.comment_id_edit = id;
    },
    async delComment(id) {
      await axios
        .delete("http://127.0.0.1:5000/delcomment/" + id._id, id)
        .finally(() => {
          this.getAllComment();
          // console.log(this.comments);
        });
    },
    editComment(id) {
      console.log(id);
      this.edit = false;
      this.comment_id_edit = null;

      axios
        .put("http://127.0.0.1:5000/editcomment/" + id._id, id)
        .finally(() => {
          this.getAllComment();
          console.log(this.comments);
        });
    },

    async getAllComment() {
      await axios
        .get("http://127.0.0.1:5000/comment/" + this.post_id)

        .then((response) => {
          this.comments = response.data;
          console.log(this.comments);
          this.isLoad = true;
          this.$forceUpdate();
        })
        .catch((error) => console.log(error));
    },
  },
  mounted() {
    this.user = this.getUID();
    console.log(this.user);
  },
  async created() {
    this.getAllComment();
  },
};
</script>
<style lang=""></style>
