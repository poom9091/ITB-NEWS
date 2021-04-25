<template lang="">
  <div>
    <button
      class="transition duration-200 ease-in-out hover:bg-red-700 flex bg-red-500 px-2 py-2 rounded-lg"
      v-on:click="login()"
    >
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
  </div>
</template>
<script>
import firebase from "firebase";
import { mapActions } from "vuex";

// firebase.initializeApp(firebaseConfig);

var provider = new firebase.auth.GoogleAuthProvider();
provider.addScope("https://www.googleapis.com/auth/contacts.readonly");
provider.setCustomParameters({
  login_hint: "user@example.com",
});
export default {
  methods: {
    ...mapActions(["setUser"]),
    async login() {
      var user = {
        uid: "",
        name: "",
      };
      await firebase
        .auth()
        .signInWithPopup(provider)
        .then((result) => {
          //   var credential = result.credential;
          var getuser = result.user;
          //   console.log(result);
          user.uid = getuser.uid;
          user.name = getuser.displayName;
          console.log(user);
          console.log("UID :: ", getuser.uid);
          console.log("displayName :: ", getuser.displayName);
          console.log("Email :: ", getuser.email);
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
