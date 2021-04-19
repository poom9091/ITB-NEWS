<template lang="">
  <div>
    <div class="p-2 px-3 border-b-2  ">
      <div
        class=" flex-row flex justify-between  text-sm font-thin text-gray-700"
      >
        <div>
          Posted by
          <button class="underline" @click="go_profile(p.user_id, p.username)">
            {{ p.username }}
          </button>
        </div>
        <div>{{ p.time }}</div>
      </div>
      <div class="text-2xl font-bold   ">{{ p.posttitle }}</div>
    </div>
    <router-link
      :to="{
        name: 'Comment',
        params: {
          _id: p._id,
        },
      }"
    >
      <div class="px-4 py-2  border-b-2">
        <div class=" text-sm font-medium truncate ">{{ p.newtitle }}</div>
        <div class=" flex space-x-2 mt-2 relative">
          <img :src="p.newimg" class=" rounded-lg w-60 " />
          <div class=" italic text-sm text-justify overflow-ellipsis">
            {{ p.newdes }}
          </div>
        </div>
      </div>

      <div class=" p-3 overflow-ellipsis overflow-auto max-h-24 border-b-2">
        {{ p.postdes }}
      </div>
    </router-link>

    <div class="flex justify-between px-3 py-2 align-middle">
      <div class="flex divide-x-2 space-x-2">
        <button
          v-if="p.vote.includes(user.uid)"
          v-on:click="dislinkcomment(p)"
          class="flex justify-between space-x-3 hover:bg-gray-300 max-w-max w-max p-2 rounded-md "
        >
          <div>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5 text-blue-400"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                d="M2 10.5a1.5 1.5 0 113 0v6a1.5 1.5 0 01-3 0v-6zM6 10.333v5.43a2 2 0 001.106 1.79l.05.025A4 4 0 008.943 18h5.416a2 2 0 001.962-1.608l1.2-6A2 2 0 0015.56 8H12V4a2 2 0 00-2-2 1 1 0 00-1 1v.667a4 4 0 01-.8 2.4L6.8 7.933a4 4 0 00-.8 2.4z"
              />
            </svg>
          </div>
          <div>{{ p.vote.length }}</div>
          <div>Vote</div>
        </button>

        <button
          v-else
          v-on:click="linkcomment(p)"
          class="flex justify-between space-x-2 hover:bg-gray-300 max-w-max w-max p-2 rounded-md "
        >
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
          <div></div>
          <div>{{ p.vote.length }}</div>
          <div>Vote</div>
        </button>

        <div class="flex justify-between max-w-max w-max space-x-2 p-2">
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
          <div>{{ p.view }}</div>
          <div>Comments</div>
        </div>
      </div>
      <div class="flex w-max max-w-max space-x-2">
        <button
          v-on:click="go_topic(p.newtitle)"
          class="transition duration-200 ease-in-out flex space-x-2 bg-gray-400 p-2 rounded-md hover:bg-blue-400 text-white"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5"
            viewBox="0 0 20 20"
            fill="currentColor"
          >
            <path
              d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2h-1.528A6 6 0 004 9.528V4z"
            />
            <path
              fill-rule="evenodd"
              d="M8 10a4 4 0 00-3.446 6.032l-1.261 1.26a1 1 0 101.414 1.415l1.261-1.261A4 4 0 108 10zm-2 4a2 2 0 114 0 2 2 0 01-4 0z"
              clip-rule="evenodd"
            />
          </svg>
          <div class=" max-w-max w-max">Topic New</div>
        </button>
        <button
          v-on:click="goURL(p.newurl)"
          class="transition duration-200 ease-in-out flex space-x-2 bg-gray-400 p-2 rounded-md hover:bg-blue-400 text-white  "
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
          <div class=" max-w-max w-max">Link to news</div>
        </button>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  props: ["p", "user"],
  created() {
    console.log(this.p);
  },
  methods: {
    go_profile(uid, name) {
      this.$router.push({ path: `/board/profile/${uid}/${name}` });
    },
    goURL(url) {
      window.location.href = url;
    },
    linkcomment(p) {
      if (this.user.uid.length == 0) {
        var r = confirm("กรุณา Login ก่อนถึงใช้งาน Feature นี้ได้");
        if (r == true) {
          this.$router.push("/login");
        } else {
          this.$router.push("/board");
        }
      } else {
        let linkcomment = {
          _id: p._id,
          uid: this.user.uid,
        };
        p.vote.push(this.user.uid);
        console.log(p);
        // api comment
        axios.put("http://127.0.0.1:81/createpost", linkcomment).finally(() => {
          this.getPostFromApi();
        });
      }
    },
    dislinkcomment(p) {
      let linkcomment = {
        _id: p._id,
        uid: this.user.uid,
      };
      var index = p.vote.indexOf(this.user.uid);
      if (index > -1) {
        p.vote.splice(index, 1);
      }
      // p.vote.pop(this.user.uid);
      console.log(p);
      // api comment
      axios.put("http://127.0.0.1:81/createpost", linkcomment).finally(() => {
        this.getPostFromApi();
      });
    },
    go_topic(newTopic) {
      this.$router.push({ path: `/board/topic_news/${newTopic}` });
    },
  },
};
</script>
<style lang=""></style>
