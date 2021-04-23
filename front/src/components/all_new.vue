<template>
  <div v-if="!isLoading">
    <!-- <div class=" text-blue-600 font-extrabold text-4xl my-3 ">
      News Today
    </div> -->
    <div v-for="n in news" :key="n.index" >
      <div class="flex flex-wrap flex-col sm:flex-row px-2 sm:px-5 py-10  ">
        <img :src="n.urlToImage" class="rounded-xl sm:w-4/12 w-full" />
        <div
          class=" w-full sm:w-7/12  flex-col flex justify-around mx-auto space-y-2 "
        >
          <div class="font-bold text-base sm:text-2xl text-black   ">
            {{ n.title }}
          </div>
          <div
            class=" text-sm sm:text-base text-black text-justify  "
          >
            {{ n.description }}
          </div>
          <div class="text-right">
            <div class=" text-xs sm:text-sm italic">
              Time : {{ n.publishedAt.slice(11, 16) }}
              {{ n.publishedAt.slice(0, 10) }}
            </div>
            <!-- <a :href="n.url" class="underline text-2xl">Link</a> -->
          </div>
          <div
            class="flex  sm:w-full justify-center sm:justify-end space-x-1 sm:space-x-5  "
          >
            <!-- <router-link to="/createboard/n.title" -->
            <router-link
              :to="{
                name: 'Create',
                params: {
                  title: n.title,
                  img: n.urlToImage,
                  des: n.description,
                  url: n.url,
                  time: `${n.publishedAt.slice(11, 16)} ${n.publishedAt.slice(
                    0,
                    10
                  )}`,
                },
              }"
              class="w-24 sm:max-w-max sm:w-max transition duration-200 ease-in-out sm:flex sm:space-x-3 border-gray-400 border-2 sm:p-3 rounded-md hover:bg-blue-400 hover:text-white"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-6 w-6 mx-auto"
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

              <div class=" font-light text-center text-xs sm:text-base">Create Board</div>
            </router-link>
            <button
              @click="go_topic(n.title)"
              class="w-24 sm:max-w-max sm:w-max transition duration-200 ease-in-out sm:flex sm:space-x-3  border-gray-400 border-2 sm:p-3 rounded-md hover:bg-blue-400 hover:text-white"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-6 w-6 mx-auto"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  fill-rule="evenodd"
                  d="M5 3a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2V5a2 2 0 00-2-2H5zm0 2h10v7h-2l-1 2H8l-1-2H5V5z"
                  clip-rule="evenodd"
                />
              </svg>
              <div class="font-light text-xs sm:text-base">All New's Board</div>
            </button>
            <button
              v-on:click="goURL(n.url)"
              class="w-24 sm:max-w-max sm:w-max transition duration-200 ease-in-out sm:flex sm:space-x-3  border-gray-400 border-2 sm:p-3 rounded-md hover:bg-blue-400 hover:text-white"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class=" h-6 w-6 mx-auto"
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

              <div class=" font-light text-xs sm:text-base">Link</div>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-else>
    <div class=" text-center text-blue-500 py-11 font-extrabold">Loading....</div>
  </div>
</template>

<script>
import { mapState } from "vuex";
// import {mapState} from 'vuex';
export default {
  computed: {
    ...mapState(["news", "isLoading"]),
  },
  methods: {
    goURL(url) {
      window.location.href = url;
    },
    go_topic(newTopic) {
      this.$router.push({ path: `/board/topic_news/${newTopic}` });
    },
  },
};
</script>

<style></style>
