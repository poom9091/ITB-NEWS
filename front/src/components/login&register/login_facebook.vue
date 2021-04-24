<template>
  <div>
    <button
      class="transition duration-200 ease-in-out hover:bg-blue-700 flex bg-blue-500 px-2 py-2 rounded-lg"
      v-on:click="sign()"
    >
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
    <div id="fb-root"></div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
import firebase from "firebase";

var provider = new firebase.auth.FacebookAuthProvider();
provider.addScope("public_profile");
provider.setCustomParameters({
  display: "popup",
});
// async defer crossorigin="anonymous" src="https://connect.facebook.net/en_US/sdk.js"
// import VFacebookLogin from 'vue-facebook-login-component'
export default {
  updated() {
    console.log(this.user.uid);
  },
  methods: {
    ...mapActions(["setUser"]),
    async sign() {
      var user = {
        uid: "",
        name: "",
      };
      await firebase
        .auth()
        .signInWithPopup(provider)
        .then(function(result) {
          // var token = result.credential.accessToken
          var getuser = result.user;

          user.uid = getuser.uid;
          user.name = getuser.displayName;
          console.log("displayName :: ", getuser.displayName);
          console.log("UID :: ", getuser.uid);
          console.log("email ::", getuser.email);
        })
        .catch(function(error) {
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

<style></style>
