<template lang="">
  <div class="px-2 lg:px-20 py-5 lg:py-10 lg:pt-20 ">
    <div
      class=" text-4xl  text-blue-600 font-extrabold px-4 pb-5 border-b-4 border-dashed border-blue-400 "
    >
      News
    </div>
    <div v-if="!isLoading" class="relative">
      <!-- <div class=" text-blue-600 font-extrabold text-4xl my-3 ">
      News Today
    </div> -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-4 py-3 ">
        <div v-for="n in news.slice(0, 1)" :key="n.index" class=" col-span-1 lg:col-span-2 ">
          <div
            :style="{
              backgroundImage:
                ' linear-gradient(to bottom, rgba(230, 243, 255,0.2),rgba(1, 1, 1, 0.6), rgba(1, 1, 1, 1)),url(' +
                n.urlToImage +
                ')',
            }"
            class=" h-72 bg-cover bg-center  bg-no-repeat flex justify-end flex-col p-2 py-5 relative rounded-xl shadow-xl"
          >
            <div class=" text-white font-bold  text-base  lg:font-black lg:text-2xl ">
              {{ n.title }}
            </div>
            <div
              class=" italic text-sm text-justify overflow-ellipsis  text-white truncate w-0  lg:w-2/3 "
            >
              {{ n.description }}
            </div>

            <div class=" lg:absolute lg:bottom-2 lg:right-5 justify-around flex flex-row-reverse ">
              <button
                v-on:click="goURL(n.url)"
                class="hover:bg-white p-1 rounded-lg text-white hover:text-black flex flex-col"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-8 w-8 m-auto"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"
                  />
                </svg>
                <div class=" text-xs">Read more</div>
              </button>

              <button
                @click="go_topic(n.title)"
                class="hover:bg-white p-1 rounded-lg text-white hover:text-black flex flex-col"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-8 w-8 m-auto"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    fill-rule="evenodd"
                    d="M5 3a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2V5a2 2 0 00-2-2H5zm0 2h10v7h-2l-1 2H8l-1-2H5V5z"
                    clip-rule="evenodd"
                  />
                </svg>
                <div class=" text-xs">All New's Board</div>
              </button>

              <button
                v-on:click="CreatePost(n)"
                class="hover:bg-white p-1 rounded-lg text-white hover:text-black flex flex-col"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-8 w-8 m-auto"
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
                <div class=" text-xs">Create Post</div>
              </button>
            </div>
          </div>
        </div>

        <div
          v-for="n in news.slice(1,loadMore)"
          :key="n.index"
          class="h-72 bg-white rounded-xl"
        >
          <div
            :style="{
              backgroundImage:
                ' linear-gradient(to bottom, rgba(230, 243, 255,0.2),rgba(1, 1, 1, 0.6), rgba(1, 1, 1, 1)),url(' +
                n.urlToImage +
                ')',
            }"
            class=" h-72 bg-cover bg-center  bg-no-repeat flex justify-end flex-col p-2 py-5 relative rounded-xl shadow-xl"
          >
            <div class="flex flex-col space-y-2">
              <div class=" text-white font-bold text-base lg:text-lg ">
                {{ n.title }}
              </div>

              <div class="  flex flex-row-reverse justify-around  ">
                <button
                  v-on:click="goURL(n.url)"
                  class="hover:bg-white p-1 rounded-lg text-white hover:text-black flex flex-col"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-8 w-8 m-auto"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"
                    />
                  </svg>
                  <div class=" text-xs">Read more</div>
                </button>

                <button
                  @click="go_topic(n.title)"
                  class="hover:bg-white p-1 rounded-lg text-white hover:text-black flex flex-col"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-8 w-8 m-auto"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M5 3a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2V5a2 2 0 00-2-2H5zm0 2h10v7h-2l-1 2H8l-1-2H5V5z"
                      clip-rule="evenodd"
                    />
                  </svg>
                  <div class=" text-xs">All New's Board</div>
                </button>

                <button
                  v-on:click="CreatePost(n)"
                  class="hover:bg-white p-1 rounded-lg text-white hover:text-black flex flex-col"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-8 w-8 m-auto"
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
                  <div class=" text-xs">Create Post</div>
                </button>
              </div>
            </div>
          </div>
        </div>
        
      </div>
      <button  class=" absolute -bottom-7 right-2 underline italic text-blue-500 " @click="loadMore+=6" >Load More ...</button>
    </div>
    <div v-else>
      <div class=" text-center text-blue-500 py-11 font-extrabold">
        Loading....
      </div>
    </div>
  </div>
</template>
<script>
import { mapState } from "vuex";
export default {
  data() {
    return {
      loadMore: 5,
    };
  },
  computed: {
    ...mapState(["news", "isLoading"]),
  },
  methods: {
    goURL(url) {
      window.location.href = url;
    },
    CreatePost(n) {
      this.$router.push({
        name: "Create",
        params: {
          title: n.title,
          img: n.urlToImage,
          des: n.description,
          url: n.url,
          time: `${n.publishedAt.slice(11, 16)} ${n.publishedAt.slice(0, 10)}`,
        },
      });
    },

    go_topic(newTopic) {
      this.$router.push({ path: `/board/topic_news/${newTopic}` });
    },
  },
};
</script>
<style lang=""></style>
