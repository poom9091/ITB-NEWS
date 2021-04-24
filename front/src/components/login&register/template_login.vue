<template lang="">
    <div class=" text-black text-2xl font-bold">Log in</div>
        <Login_facebook />
        <Login_Google />

        <div class=" flex ">
          <svg height="10" width="1000" class=" my-auto ">
            <line
              x1="0"
              y1="5"
              x2="1000"
              y2="5"
              class=" stroke-current text-gray-400"
            />
          </svg>
          <div class=" px-6 my-auto text-gray-400 ">or</div>
          <svg height="10" width="1000" class=" my-auto ">
            <line
              x1="0"
              y1="5"
              x2="1000"
              y2="5"
              class=" stroke-current text-gray-400"
            />
          </svg>
        </div>
        <Login />
        <router-link
          to="/login/register"
          class="transition duration-200 ease-in-out font-semibold text-gray-500 border-2 rounded-lg p-2 hover:bg-gray-400 hover:text-white text-center "
        >
          Create account
        </router-link>
        <button class=" text-sm text-gray-500 underline w-full text-right px-4">
          Forget password
        </button>
</template>
<script>
import Login_facebook from "../login&register/login_facebook.vue";
import Login_Google from "../login&register/login_google.vue";
import Login from "../login&register/login";
export default {
    components: {
    Login_facebook,
    Login_Google,
    Login,
  },
}
</script>
<style lang="">
    
</style>