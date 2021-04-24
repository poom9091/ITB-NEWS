<template>
  <div>
    <div class="flex bg-blue-600 py-2 text-white justify-between px-3 sm:px-7 h-14 sm:h-16 ">
      <div class=" my-auto space-x-2 ">
        <router-link class=" font-extrabold text-lg md:text-2xl"  to="/">ITB-NEW<h1 class=" inline-block text-red-500">S</h1></router-link>
        <router-link
          class="transition duration-300 ease-in-out p-2 px-3 rounded-xl text-lg font-semibold  my-auto
                        hover:bg-white hover:bg-opacity-20 invisible h-0 w-0 md:visible "
          to="/"
        >
          Home</router-link
        >
      </div>
      <div class="flex space-x-4 text-sm md:text-lg font-semibold  ">
        
        <router-link
          class="transition duration-300 ease-in-out p-2 px-3 rounded-xl h-10 sm:my-auto  
                        hover:bg-white hover:bg-opacity-20 "
          to="/board"
        >
          Board</router-link
        >
        <router-link
          class="transition duration-300 ease-in-out p-2 px-3 rounded-xl h-10 sm:my-auto 
                        hover:bg-white hover:bg-opacity-20 "
          to="/news"
          >News</router-link
        >
        
        <router-link
          v-if=" this.user.uid == null"
          class="transition duration-300 ease-in-out p-1 rounded-xl
                        bg-white text-blue-500 px-3 border-4 border-blue-600
                        hover:bg-blue-600 hover:text-white "
          to="/login"
          >Login</router-link
        >
        <profile_d v-else />
      </div>
      
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import profile_d from "../components/Profile_dropdown"
export default {
  name: "Navbar",
  components:{
    profile_d
  },
  computed: {
    ...mapState(["user"]),
  },
  mounted() {
  },
};
</script>

<style></style>
