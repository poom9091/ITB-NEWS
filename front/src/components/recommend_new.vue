<template>
  <div class="flex space-x-5">
      <svg height="10" width="1000"  class=" my-auto w-1/12 ">
          <line
            x1="0" y1="5" x2="1000" y2="5"
            class=" stroke-current text-blue-400 "
          />
        </svg>
      <div class=" text-blue-800 font-extrabold text-4xl">Recommend News</div>
      <svg height="10" width="1000"  class=" my-auto w-7/12">
          <line
            x1="0" y1="5" x2="1000" y2="5"
            class=" stroke-current text-blue-400"
          />
        </svg>
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
}
</script>

<style>

</style>