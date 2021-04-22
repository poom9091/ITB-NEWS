<template>
  <div>
    <div class="flex bg-blue-600 py-2 text-white justify-between  px-7">
      <div class=" my-auto space-x-2">
        <router-link class=" font-extrabold text-2xl"  to="/">ITB-NEWS</router-link>
        <router-link
          class="transition duration-300 ease-in-out p-2 px-3 rounded-xl text-lg font-semibold  my-auto
                        hover:bg-white hover:bg-opacity-20 "
          to="/"
        >
          Home</router-link
        >
      </div>
      <div class="flex space-x-4 text-lg font-semibold ">
        
        <router-link
          class="transition duration-300 ease-in-out p-2 px-3 rounded-xl  my-auto
                        hover:bg-white hover:bg-opacity-20 "
          to="/board"
        >
          Board</router-link
        >
        <router-link
          class="transition duration-300 ease-in-out p-2 px-3 rounded-xl my-auto
                        hover:bg-white hover:bg-opacity-20 "
          to="/news"
          >News Today</router-link
        >
        

        <!-- <router-link
          v-else
          class="transition duration-300 ease-in-out p-2 rounded-xl flex space-x-2
                        bg-white text-blue-500 px-3 border-4 border-blue-600
                        hover:bg-blue-600 hover:text-white "
          to="/login"
        >
          <div>Logout</div>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-7 w-7"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"
            />
          </svg>
        </router-link> -->
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
