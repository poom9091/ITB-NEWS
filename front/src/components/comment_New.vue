<template>
  <div class=" my-auto">
    <div v-if="isLoad" class=" border-gray-500 rounded-md border-2  divide-y ">
      <div class="p-4 px-6">
        <div
          class=" flex-row flex justify-between text-sm font-thin text-gray-500 "
        >
          <div>Posted by {{ detail.username }}</div>
          <div>{{ detail.time }}</div>
        </div>
        <div class="text-4xl font-bold   ">{{ detail.posttitle }}</div>
      </div>
      <div class="px-4 py-2 ">
        <div class=" text-sm font-medium truncate ">{{ detail.newtitle }}</div>
        <div class=" flex space-x-2 mt-2 relative">
          <img :src="detail.newimg" class=" rounded-lg w-60 " />
          <div class=" italic text-sm text-justify overflow-ellipsis px-6">
            {{ detail.newdes }}
          </div>
          <div class=" flex flex-col space-y-2 px-3 w-80">
            <button
              v-on:click="goURL(detail.newurl)"
              class="transition duration-200 ease-in-out flex space-x-1 bg-gray-400 p-2 rounded-md hover:bg-blue-400 text-white "
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
            <button
              v-on:click="goURL(detail.newurl)"
              class="transition duration-200 ease-in-out flex space-x-1 bg-gray-400 p-2 rounded-md hover:bg-blue-400 text-white "
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
              <div>All post</div>
            </button>
          </div>
        </div>
      </div>
      <div class=" p-6 overflow-ellipsis overflow-auto max-h-24">
        {{ detail.postdes }}
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
          <div>{{ detail.view }}</div>
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
        this.isLoad = false;
        this.isLoad = true;
        this.$forceUpdate();
      })
      .catch((error) => console.log(error));
  },
};
</script>

<style></style>
