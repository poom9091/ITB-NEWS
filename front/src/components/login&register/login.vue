<template lang="">
  <input
    v-model="email"
    class=" bg-gray-200 rounded-lg p-3"
    placeholder="Email"
  />
  <input
    v-model="password"
    type="password"
    class=" bg-gray-200 rounded-lg p-3 "
    placeholder="Password"
  />
  <button
    class=" flex bg-gray-500 px-2 py-2 rounded-lg transition duration-200 ease-in-out hover:bg-gray-700"
    v-on:click="login()"
  >
    <svg
      xmlns="http://www.w3.org/2000/svg"
      class=" h-6 text-white w-2/12 my-auto"
      fill="none"
      viewBox="0 0 24 24"
      stroke="currentColor"
    >
      <path
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="2"
        d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"
      />
    </svg>
    <div class="  text-white font-semibold w-10/12 my-auto">
      Login with Email
    </div>
  </button>
</template>
<script>
import { mapActions } from "vuex";
import firebase from "firebase";
export default {
  email: "",
  password: "",
  methods: {
    ...mapActions(["setUser"]),
    async login() {
      var user = {
        uid: "",
        name: "",
      };
      await firebase
        .auth()
        .signInWithEmailAndPassword(this.email, this.password)
        .then((userCredential) => {
          // Signed in
          var getuser = userCredential.user;
          user.uid = getuser.uid;
          user.name = getuser.displayName;
          console.log(getuser);
          // ...
        })
        .catch((error) => {
          console.log(error);
        });
      this.setUser(user);
      localStorage.uid = user.uid
      localStorage.name = user.name
      this.$router.push("/");
    },
  },
};
</script>
<style lang=""></style>
