<template>
  <div class=" my-auto">
    <div v-if="isLoad" class=" divide-y">
      <div
        :style="{
          backgroundImage:
            ' linear-gradient(to bottom, rgba(230, 243, 255,0.2),rgba(1, 1, 1, 0.6), rgba(1, 1, 1, 1)),url(' +
            detail.newimg +
            ')',
        }"
        class=" h-72 bg-cover bg-top flex justify-end flex-col p-2 py-5 relative"
      >
        <div class=" text-white font-black text-2xl ">
          {{ detail.newtitle }}
        </div>
        <div
          class=" italic text-sm text-justify overflow-ellipsis  text-white truncate pr-20"
        >
          {{ detail.newdes }}
        </div>
        <button
          v-on:click="goURL(detail.newurl)"
          class=" absolute bottom-2 right-5 hover:bg-white p-1 rounded-lg text-white hover:text-black flex"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-8 w-8 "
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
        </button>
      </div>

      <div class="p-4 py-2  ">
        <div
          class=" flex-row flex justify-between text-sm font-thin text-gray-500 "
        >
          <div>Posted by {{ detail.username }}</div>
          <div>{{ detail.time }}</div>
        </div>
        <div class="text-4xl font-bold   ">{{ detail.posttitle }}</div>
        <div class=" py-2 ">
          {{ detail.postdes }}
        </div>
      </div>

      <div
        class="flex space-x-2 px-4 py-3  divide-x-2  divide-gray-500 "
      >
        <div class="flex  space-x-2 px-2">
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
          <div>{{ detail.view }}</div>
          <div>Vote</div>
        </div>

        <div class="flex  space-x-2 px-2">
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
          <div>{{ detail.vote }}</div>
          <div>Comments</div>
        </div>
      </div>
    </div>
    <div v-else>
      loading..
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  props: ["detail_n"],
  detail: null,
  isLoad: false,
  methods: {
    goURL(url) {
      window.location.href = url;
    },
  },
  async created() {
    await axios
      .get("https://api.jsonbin.io/b/6076d93d0ed6f819beac0f9f", {
        headers: {
          "secret-key":
            "$2b$10$pJX92cjXZes3hSYfvlbp5e1xRhcBEEUNb3iGF8AAaXms5LFcB6mu2",
        },
      })
      .then((response) => {
        this.detail = response.data;
        console.log(this.detail);
        this.isLoad = true;
        this.$forceUpdate();
      })
      .catch((error) => console.log(error));
  },
};
</script>

<style></style>
