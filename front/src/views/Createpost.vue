<template>
  <div class=" h-screen bg-gray-300 py-24">
    <div class="bg-white rounded-md  max-w-2xl mx-auto p-6 shadow-2xl">
      <div class=" text-3xl font-semibold text-blue-400">Create Post</div>
      <div class="flex flex-col space-y-4 py-2 justify-around">
        <div class=" text-3xl font-semibold">{{ $route.params.title }}</div>
        <img
          :src="$route.params.img"
          class="rounded-xl w-96 m-auto shadow-lg "
        />
        <div class=" flex flex-row space-x-3 px-4">
          <div class=" max-w-max w-max  text-base font-medium my-auto">
            Topic
          </div>
          <input
            id="title"
            class=" w-full border-2  p-2 text-black rounded-md border-dashed focus:border-transparent focus:outline-none focus:ring-2 focus:ring-blue-300"
            placeholder="Title"
          />
        </div>
        <div class=" flex flex-row space-x-3 px-4">
          <div class=" max-w-max w-max  text-base font-medium my-auto">
            Description
          </div>
          <input
            id="title"
            class=" w-full border-2  p-2 text-black rounded-md border-dashed focus:border-transparent focus:outline-none focus:ring-2 focus:ring-blue-300"
            placeholder="Description"
          />
        </div>
        <div class=" flex flex-row space-x-3 justify-end">
          <button
            class="transition duration-200 border-2 border-blue-600 bg-blue-400  p-3 py-2 rounded-lg text-white text-base font-semibold transform  hover:-translate-y-1  hover:scale-110"
          >
            Create
          </button>
          <button
            class="transition duration-200 border-2 border-gray-600  p-3 py-2 rounded-lg  text-base font-semibold bg-white text-black transform  hover:-translate-y-1 hover:scale-110"
          >
            Cancle
          </button>
        </div>
      </div>
    </div>
    <div></div>
  </div>
</template>

<script>
export default {};
</script>

<style></style>
