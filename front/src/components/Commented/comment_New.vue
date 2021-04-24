<template>
  <div class=" my-auto">
    <div v-if="isLoad" class=" divide-y">
      <div
        :style="{
          backgroundImage:
            ' linear-gradient(to bottom, rgba(230, 243, 255,0.2),rgba(1, 1, 1, 0.6), rgba(1, 1, 1, 1)),url(' +
            detail[0].newimg +
            ')',
        }"
        class=" h-72 bg-cover bg-top flex justify-end flex-col p-2 py-5 relative"
      >
        <div class=" text-white font-black text-lg sm:text-2xl ">
          {{ detail[0].newtitle }}
        </div>
        <div
          class=" italic text-sm text-justify overflow-ellipsis  text-white truncate pr-20"
        >
          {{ detail[0].newdes }}
        </div>

        <button
          v-on:click="goURL(detail[0].newurl)"
          class=" absolute bottom-2 right-5 hover:bg-white p-1 rounded-lg text-white hover:text-black flex"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-8 w-8 "
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"
            />
          </svg>
        </button>
      </div>

      <div class="p-4 py-2  ">
        <div
          class=" flex-row flex justify-between text-sm font-thin text-gray-500 "
        >
          <div>Posted by {{ detail[0].username }}</div>
          <div>{{ detail[0].time }}</div>
        </div>
        <div v-if="!edit">
          <div class="text-4xl font-bold   ">{{ detail[0].posttitle }}</div>
          <div class=" py-2 ">
            {{ detail[0].postdes }}
          </div>
        </div>

        <div v-else>
          <textarea
            class="text-4xl font-bold border-gray-400 border-2 rounded-md border-dashed px-2 py-1 w-full "
            v-model="detail[0].posttitle"
            rows="2"
          >
          </textarea>
          <textarea
            class=" py-2 px-2 w-full mt-2 border-2 rounded-md border-dashed border-gray-400   "
            v-model="detail[0].postdes"
            rows="4"
          >
          </textarea>
          <div class="space-x-2 text-right">
            <button
              class="p-1 px-3 text-white rounded-md bg-blue-500 hover:bg-blue-800"
              v-on:click="editPost()"
            >
              Save
            </button>
            <button
              class="p-1 px-3 text-white rounded-md bg-gray-500 hover:bg-gray-800"
              v-on:click="this.edit = false"
            >
              Cancel
            </button>
          </div>
        </div>
      </div>

      <div
        v-if="!edit"
        class="flex flex-wrap flex-col-reverse  md:flex-row  justify-between  md:px-4 md:py-3 "
      >
        <div
          class=" flex divide-x  w-full md:max-w-max  justify-center   items-center space-x-2 sm:space-x-3 divide-gray-500"
        >
          <button
            v-if="detail[0].vote.includes(user.uid)"
            v-on:click="dislinkcomment(detail[0])"
            class="flex justify-between items-center space-x-2 hover:bg-gray-300 max-w-max w-max   rounded-md  p-2"
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
            <div class="text-xs sm:text-base">{{ detail[0].vote.length }}</div>
            <div class=" text-xs sm:text-base">Vote</div>
          </button>

          <button
            v-else
            v-on:click="linkcomment(detail[0])"
            class="flex justify-between items-center space-x-2 hover:bg-gray-300 max-w-max w-max  p-2 rounded-md "
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
            <div class=" text-xs sm:text-base">{{ detail[0].vote.length }}</div>
            <div class=" text-xs sm:text-base">Vote</div>
          </button>

          <div class="flex space-x-2 items-center max-w-max w-max py-2 p-2 ">
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
            <div class="text-xs sm:text-base">
              {{ detail[0].comment.length }}
            </div>
            <div class="text-xs sm:text-base">Comments</div>
          </div>

          <div class="flex space-x-2 items-center max-w-max w-max p-2 ">
            <div>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5 text-gray-400 m-auto"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                />
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
                />
              </svg>
            </div>
            <div class="text-xs sm:text-base">{{ detail[0].view }}</div>
            <div class="text-xs sm:text-base">View</div>
          </div>
        </div>
        <div v-if="detail[0].user_id === user.uid" class="w-full md:max-w-max ">
          <div
            class="flex justify-end items-center space-x-3  p-2 h-full border-b-2 md:border-b-0    "
          >
            <button
              class="text-gray-400 hover:text-gray-800 flex space-x-1"
              v-on:click="this.edit = true"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5 "
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z"
                />
              </svg>
              <div>Edit</div>
            </button>
            <button
              class="text-gray-400 hover:text-gray-800 flex space-x-1"
              v-on:click="deletePost(detail[0])"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  fill-rule="evenodd"
                  d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z"
                  clip-rule="evenodd"
                />
              </svg>
              <div>Delete</div>
            </button>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      loading..
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapGetters, mapActions } from "vuex";
export default {
  data() {
    return {
      edit: false,
      detail: null,
      isLoad: false,
      user: {
        uid: null,
        name: null,
      },
    };
  },
  props: ["post_id"],

  methods: {
    ...mapActions(["getPostFromApi"]),
    goURL(url) {
      window.location.href = url;
    },
    async deletePost(comment) {
      console.log(comment);
      await axios
        .delete("http://127.0.0.1:5000/delpost/" + this.post_id)
        .finally(() => {
          this.$router.push("/board");
        });
      await this.getPostFromApi();
    },
    async editPost() {
      // console.log(this.detail);
      // this.isLoad = false;
      this.edit = false;
      this.$forceUpdate();
      await axios
        .put("http://127.0.0.1:5000/editpost/" + this.post_id, this.detail[0])
        .finally(() => {
          this.getNew();
          console.log(this.detail[0]);
        });
    },
    linkcomment(detail) {
      if (this.user.uid == null) {
        var r = confirm("กรุณา Login ก่อนถึงใช้งาน Feature นี้ได้");
        if (r == true) {
          this.$router.push("/login");
        }
      } else {
        let linkcomment = {
          _id: detail._id,
          uid: this.user.uid,
        };
        detail.vote.push(this.user.uid);
        console.log(detail);

        axios
          .put("http://127.0.0.1:5000/createpost", linkcomment)
          .finally(() => {
            this.getNew();
          });
      }
    },
    dislinkcomment(detail) {
      let linkcomment = {
        _id: detail._id,
        uid: this.user.uid,
      };
      var index = detail.vote.indexOf(this.user.uid);
      if (index > -1) {
        detail.vote.splice(index, 1);
      }
      // p.vote.pop(this.user.uid);
      console.log(detail);
      axios.put("http://127.0.0.1:5000/createpost", linkcomment).finally(() => {
        this.getNew();
      });
    },

    async getNew() {
      let post_id1 = { _id: this.post_id };
      await console.log(post_id1);
      await axios
        .get("http://127.0.0.1:5000/gpost/" + this.post_id)

        .then((response) => {
          this.detail = response.data;
          console.log(this.detail);
          this.isLoad = true;
          this.$forceUpdate();
        })
        .catch((error) => console.log(error));
    },
    ...mapGetters(["getUID"]),
  },
  created() {
    console.log(this.post_id);
    this.user = this.getUID();
    this.getNew();
  },
};
</script>

<style></style>
