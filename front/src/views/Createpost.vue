<template>
  <div class=" h-full bg-gray-300 pt-24 pb-10">
    <div class="bg-white rounded-md  max-w-2xl mx-auto p-6 shadow-2xl">
      <div class=" text-3xl font-semibold text-blue-400">Create Post</div>
      <div class="flex flex-col space-y-4 py-2 justify-around">
        <div class=" text-2xl font-semibold">{{ this.title }}</div>
        <img
          :src="this.img"
          class="rounded-xl w-96 m-auto shadow-lg "
        />
        <div class=" flex flex-row space-x-3 px-4">
          <div id=topic class=" max-w-max w-max  text-base font-medium my-auto">
            Topic
          </div>
          <input
            v-model="this.ptitle"
            id="title"
            class=" w-full border-2  p-2 text-black rounded-md border-dashed focus:border-transparent focus:outline-none focus:ring-2 focus:ring-blue-300"
            placeholder="Title"
          />
        </div>
        <div class=" flex flex-row space-x-3 px-4">
          <div id='des' class=" max-w-max w-max  text-base font-medium my-auto">
            Description
          </div>
          <textarea
            v-model="this.pdes"
            rows="4"
            id="title"
            class=" w-full border-2  p-2 text-black rounded-md border-dashed focus:border-transparent focus:outline-none focus:ring-2 focus:ring-blue-300"
            placeholder="Description"
          />
        </div>
        <div class=" flex flex-row space-x-3 justify-end">
          <button
            v-on:click='createpost()'
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
  </div>
</template>

<script>
import axios from "axios";

export default {
  title: '',
  img: 'start',
  des: '',
  url: '',
  time: '',
  ptitle:'',
  pdes:'',
  created(){
    this.title = this.$route.params.title
    this.img = this.$route.params.img
    this.des = this.$route.params.des
    this.url = this.$route.params.url
    this.time = this.$route.params.time
    if(this.url==null){
      this.$router.push('/')
    }
  },
  methods:{
    createpost(){
      const newinfo = {
        newtitle : this.title,
        newimg : this.img,
        newdes : this.des,
        newurl : this.url,
        newtime : this.time,
        posttitle : this.ptitle,
        postdes : this.pdes
      };
      axios.post("https://reqres.in/invalid-url",newinfo)
      .then(response => this.newinfo = response.data)
      console.log(newinfo);
    },
    
  }
};
</script>

<style></style>
