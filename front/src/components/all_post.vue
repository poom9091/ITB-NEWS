<template>
  <div v-if="!isLoading_post" class=" px-3">
    <router-link
      v-for="p in posts"
      :key="p.index"
      :to="{
        name: 'Comment',
        params: {
          _id: p._id,
        },
      }"
      class=" bg-white rounded-xl border-4 hover:border-black divide-y"
    >
      <div class="p-2 px-3">
        <div
          class=" flex-row flex justify-between  text-sm font-thin text-gray-700"
        >
          <div>Posted by {{ p.username }}</div>
          <div>{{ p.time }}</div>
        </div>
        <div class="text-2xl font-bold   ">{{ p.posttitle }}</div>
      </div>
      <div class="px-4 py-2 ">
        <div class=" text-sm font-medium truncate ">{{ p.newtitle }}</div>
        <div class=" flex space-x-2 mt-2 relative">
          <img :src="p.newimg" class=" rounded-lg w-60 " />
          <div class=" italic text-sm text-justify overflow-ellipsis">
            {{ p.newdes }}
          </div>
          <button
            v-on:click="goURL(p.newurl)"
            class="transition duration-200 ease-in-out flex space-x-2 bg-gray-400 p-2 rounded-md hover:bg-blue-400 text-white  absolute right-2 bottom-2"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class=" h-6 w-6 "
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                d="M11 3a1 1 0 100 2h2.586l-6.293 6.293a1 1 0 101.414 1.414L15 6.414V9a1 1 0 102 0V4a1 1 0 00-1-1h-5z"
              />
              <path
                d="M5 5a2 2 0 00-2 2v8a2 2 0 002 2h8a2 2 0 002-2v-3a1 1 0 10-2 0v3H5V7h3a1 1 0 000-2H5z"
              />
            </svg>
            <div>Link</div>
          </button>
        </div>
      </div>

      <div class=" p-3 overflow-ellipsis overflow-auto max-h-24">
        {{ p.postdes }}
      </div>

      <div class="flex justify-star space-x-14 px-3 py-1 align-middle">
        <div class="flex justify-between w-10 space-x-2">
          <div>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5 text-gray-400"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                d="M2 10.5a1.5 1.5 0 113 0v6a1.5 1.5 0 01-3 0v-6zM6 10.333v5.43a2 2 0 001.106 1.79l.05.025A4 4 0 008.943 18h5.416a2 2 0 001.962-1.608l1.2-6A2 2 0 0015.56 8H12V4a2 2 0 00-2-2 1 1 0 00-1 1v.667a4 4 0 01-.8 2.4L6.8 7.933a4 4 0 00-.8 2.4z"
              />
            </svg>
          </div>
          <div>{{ p.view }}</div>
          <div>Vote</div>
        </div>
        <div class="flex justify-between w-10 space-x-2">
          <div>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5 text-gray-400"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                fill-rule="evenodd"
                d="M18 13V5a2 2 0 00-2-2H4a2 2 0 00-2 2v8a2 2 0 002 2h3l3 3 3-3h3a2 2 0 002-2zM5 7a1 1 0 011-1h8a1 1 0 110 2H6a1 1 0 01-1-1zm1 3a1 1 0 100 2h3a1 1 0 100-2H6z"
                clip-rule="evenodd"
              />
            </svg>
          </div>
          <div>{{ p.vote }}</div>
          <div>Comments</div>
        </div>
      </div>
    </router-link>
  </div>
  <div v-else>
    <div>Loading....</div>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  computed: {
    ...mapState(["posts", "isLoading_post"]),
  },
  methods: {
    goURL(url) {
      window.location.href = url;
    },
  },
  mounted() {
    console.log(this.posts);
  },
};
</script>

<style></style>
