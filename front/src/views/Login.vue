<template>
  <div class=" flex flex-wrap mt-28">
    <div
      class=" mx-auto  px-5 py-6 rounded-lg flex flex-col relative border-blue-900 border-4 w-96 space-y-4"
    >
      <div class=" text-black text-2xl font-bold">Log in</div>
      <button class=" flex bg-blue-500 px-2 py-2 rounded-lg">
        <svg
          class="fill-current h-6 text-white w-2/12 my-auto"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
        >
          <path
            d="M24 12a12 12 0 10-13.9 12v-8.5h-3v-3.4h3V9.4c0-3 1.8-4.6 4.6-4.6l2.6.2v3h-1.5c-1.5 0-2 .9-2 1.8v2.3h3.4l-.5 3.4h-2.8V24A12 12 0 0024 12.1z"
          />
        </svg>
        <div class=" text-white font-semibold w-10/12 my-auto">
          Login with Facebook
        </div>
      </button>
      <button class=" flex bg-red-500 px-2 py-2 rounded-lg">
        <svg
          class="fill-current h-6 text-white w-2/12 my-auto"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M12.5 11v3.2h7.8a7 7 0 01-1.8 4.1 8 8 0 01-6 2.4c-4.8 0-8.6-3.9-8.6-8.7a8.6 8.6 0 0114.5-6.4l2.3-2.3C18.7 1.4 16 0 12.5 0 5.9 0 .3 5.4.3 12S6 24 12.5 24a11 11 0 008.4-3.4c2.1-2.1 2.8-5.2 2.8-7.6 0-.8 0-1.5-.2-2h-11z"
          />
        </svg>
        <div class=" text-white font-semibold w-10/12 my-auto">
          Login with Google
        </div>
      </button>
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
        <svg height="10" width="1000"  class=" my-auto ">
          <line
            x1="0"
            y1="5"
            x2="1000"
            y2="5"
            class=" stroke-current text-gray-400"
          />
        </svg>
      </div>
      <input v-model="email" class=" bg-gray-200 rounded-lg p-3" placeholder="Email">
      <input v-model="password" type="password" class=" bg-gray-200 rounded-lg p-3" placeholder="Password">
      <button class=" flex bg-gray-500 px-2 py-2 rounded-lg">
          <svg xmlns="http://www.w3.org/2000/svg" class=" h-6 text-white w-2/12 my-auto" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1" />
            </svg>
        <div class=" text-white font-semibold w-10/12 my-auto">
          Login with Email
        </div>
      </button>
    </div>
    
  </div>
</template>

<script>
export default {
    email:'',
    password:''
};
</script>

<style></style>
