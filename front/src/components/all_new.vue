<template>
  <div v-if="!isLoading">
    <div class=" text-blue-600 font-extrabold text-4xl my-3 ">
      News Today
    </div>
    <div v-for="(n) in news" :key="n.index"  >
      <div class="flex flex-wrap p-5 my-3 ">
        <img :src="n.urlToImage" class="rounded-xl w-4/12 " />
        <div class="w-7/12  flex-col flex justify-around mx-auto ">
          <div class="font-bold text-2xl text-black ">{{ n.title }}</div>
          <div class=" text-base text-black ">{{ n.description }}</div>
          <div class="text-right">
            <div>{{ n.publishedAt }}</div>
            <!-- <a :href="n.url" class="underline text-2xl">Link</a> -->
          </div>
          <div class="flex w-full justify-end space-x-5  ">
            <!-- <router-link to="/createboard/n.title" -->
              <router-link
                :to="{
                  name: 'Create',
                  params: {
                    title: n.title,
                    img: n.urlToImage,
                    des: n.description,
                    url: n.url,
                    time: n.publishedAt,
                  },
                }"
                class=" transition duration-200 ease-in-out flex space-x-3  border-gray-400 border-2 p-3 rounded-md hover:bg-blue-400 hover:text-white"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-6 w-6 "
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    d="M17.414 2.586a2 2 0 00-2.828 0L7 10.172V13h2.828l7.586-7.586a2 2 0 000-2.828z"
                  />
                  <path
                    fill-rule="evenodd"
                    d="M2 6a2 2 0 012-2h4a1 1 0 010 2H4v10h10v-4a1 1 0 112 0v4a2 2 0 01-2 2H4a2 2 0 01-2-2V6z"
                    clip-rule="evenodd"
                  />
                </svg>

                <div class=" font-light">Create Board</div>
              </router-link>
              <button
                class=" transition duration-200 ease-in-out flex space-x-3  border-gray-400 border-2 p-3 rounded-md hover:bg-blue-400 hover:text-white"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-6 w-6"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    fill-rule="evenodd"
                    d="M5 3a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2V5a2 2 0 00-2-2H5zm0 2h10v7h-2l-1 2H8l-1-2H5V5z"
                    clip-rule="evenodd"
                  />
                </svg>
                <div class="font-light">All New's Board</div>
              </button>
              <button
                v-on:click="goURL(n.url)"
                class="transition duration-200 ease-in-out flex space-x-3  border-gray-400 border-2 p-3 rounded-md hover:bg-blue-400 hover:text-white"
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
                <div class=" font-light">Link</div>
              </button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-else>
    <div>Loading....</div>
  </div>
</template>

<script>
import { mapState } from "vuex";
// import {mapState} from 'vuex';
export default {
  newshow:7,
  computed: {
    ...mapState(["news", "isLoading"]),
  },
  methods: {
    goURL(url) {
      window.location.href = url;
    },
  },
  
};
</script>

<style></style>
