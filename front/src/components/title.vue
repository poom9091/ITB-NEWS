<template>
  <div class=" h-96  bg-blue-500  flex shadow-2xl  ">
    <div class=" flex h-full w-full  pt-24  justify-around  relative ">
      <div class=" flex flex-col space-y-16 ">
        <div>
          <div class=" text-white font-extrabold text-7xl  ">
            ITB-NEW<h1 class=" inline-block text-red-500">S</h1>
          </div>
          <div class=" italic text-2xl text-white  ">desc</div>
        </div>
        <div class=" space-x-16  left-16 ">
          <router-link
            to="/board"
            class="text-white font-extrabold bg-blue-400  text-3xl py-3 p-5 rounded-md hover:bg-white hover:bg-opacity-10 shadow-lg"
          >
            Board
          </router-link>

          <router-link
            to="/news"
            class="text-white font-extrabold bg-blue-400 text-3xl  py-3 p-5 rounded-md hover:bg-white hover:bg-opacity-10 shadow-lg"
          >
            News
          </router-link>
        </div>
      </div>


      <div class=" flex  -mt-6 invisible  lg:visible w-0 h-0 lg:max-w-max lg:w-max ">
        <img class="select-none p-2 rounded-2xl m-auto " src="../assets/newsssss333.png">
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
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
