<template>
  <div class=" h-full pt-24 pb-10">
    <div
      class=" border-blue-800 border-4 rounded-md font  max-w-2xl mx-auto p-6 shadow-2xl"
    >
      <div class=" text-3xl  text-blue-700 font-extrabold">Create Post</div>

      <div class="flex flex-col space-y-4 py-2 justify-around">
        <div class=" text-2xl font-semibold ">{{ this.title }}</div>
        <img :src="this.img" class="rounded-xl w-96 m-auto shadow-lg " />
        <div class=" flex flex-row flex-wrap  px-4">
          <div
            id="topic"
            class=" max-w-max w-max  text-base font-medium my-auto"
          >
            Topic
          </div>
          <input
            v-model="this.ptitle"
            id="title"
            class=" w-full border-2 border-indigo-300 p-2 text-black rounded-md border-dashed focus:border-transparent focus:outline-none focus:ring-2 focus:ring-blue-300"
            placeholder="Title"
          />
        </div>
        <div class=" flex flex-row flex-wrap  px-4 content-start">
          <div id="des" class=" max-w-max w-max  text-base font-medium my-auto">
            Description
          </div>
          <textarea
            v-model="this.pdes"
            rows="4"
            id="title"
            class=" w-full border-2  p-2 text-black border-indigo-300 rounded-md border-dashed focus:border-transparent focus:outline-none focus:ring-2 focus:ring-blue-300"
            placeholder="Description"
          />
        </div>
        <div class=" flex flex-row space-x-3 justify-end">
          <div
            v-if="!this.ptitle"
            class="transition duration-200 border-2 border-gray-600 bg-gray-400  p-3 py-2 rounded-lg text-white text-base font-semibold"
          >
            Create
          </div>
          <button
            v-else
            v-on:click="createpost()"
            class="transition duration-200 border-2 border-blue-600 bg-blue-400  p-3 py-2 rounded-lg text-white text-base font-semibold transform  hover:-translate-y-1  hover:scale-110"
          >
            Create
          </button>
          <button
            v-on:click="this.$router.push({ path: '/news' })"
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
import { mapGetters, mapActions } from "vuex";
export default {
  data() {
    return {
      user: {
        uid: null,
        name: null,
      },
      ptitle: "",
    };
  },
  title: "",
  img: "start",
  des: "",
  url: "",
  time: "",

  pdes: "",
  created() {
    this.title = this.$route.params.title;
    this.img = this.$route.params.img;
    this.des = this.$route.params.des;
    this.url = this.$route.params.url;
    this.time = this.$route.params.time;
    if (this.url == null) {
      this.$router.push("/");
    }
    this.user = this.getUID();
  },
  mounted() {
    console.log(this.user.uid);
    console.log(this.user.name);
    if (this.user.uid == null) {
      var r = confirm("กรุณา Login ก่อนสร้าง Post");
      if (r == true) {
        this.$router.push("/login");
      } else {
        this.$router.push("/news");
      }
    }
  },

  methods: {
    ...mapActions(["getPostFromApi"]),
    ...mapGetters(["getUID"]),
    go_profile() {},
    async createpost() {
      const newinfo = {
        user_id: this.getUID().uid,
        username: this.getUID().name,
        newtitle: this.title,
        newimg: this.img,
        newdes: this.des,
        newurl: this.url,
        newtime: this.time,
        posttitle: this.ptitle,
        postdes: this.pdes,
      };
      await axios
        .post("http://127.0.0.1:5000/createpost", newinfo)

        .then((response) => (this.newinfo = response.data));
      console.log(newinfo);
      await this.getPostFromApi();
      await this.$router.push({
        path: `/board/profile/${this.getUID().uid}/${this.getUID().name}`,
      });
      // await this.$router.push({ path: '/board' })
    },
  },
};
</script>

<style></style>
