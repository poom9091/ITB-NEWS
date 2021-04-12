<template lang="">
  <div class=" text-black text-2xl font-bold">Register</div>
  <input
    v-model="email"
    class=" bg-gray-200 rounded-lg p-3"
    placeholder="Email"
  />
  <input
    v-model="username"
    class=" bg-gray-200 rounded-lg p-3"
    placeholder="Username"
  />
  <input
    v-model="password"
    type="password"
    class=" bg-gray-200 rounded-lg p-3 "
    placeholder="Password"
  />
  <input
    v-model="comfirmpassword"
    type="password"
    class=" bg-gray-200 rounded-lg p-3 "
    placeholder="Comfirm Password"
  />
  <button
    v-on:click="check()()"
    class="transition duration-200 ease-in-out bg-blue-500 font-semibold text-white border-2 rounded-lg p-2 hover:bg-blue-700 border-blue-900 text-center "
  >
    Create account
  </button>
  <router-link
    to="/login"
    class=" text-sm text-gray-500 underline w-full text-right px-4"
  >
    Cancle
  </router-link>
</template>
<script>
import firebase from "firebase";

export default {
  email: "",
  username: "",
  password: "",
  comfirmpassword:"",
  methods: {
    check(){
      if(this.comfirmpassword!==this.password){
        alert('Password not match')
      }else{
         this.register()
      }
    },
    async register() {
      await firebase
        .auth()
        .createUserWithEmailAndPassword(this.email, this.password)
        .then((userCredential) => {
          var user = userCredential.user;
          console.log(user.uid);
          console.log(user.displayName);
          this.$router.push("/login");
          alert("Successfully registered! Please login.");
        })
        .catch((error) => {
          alert(error.message);
        });
      await firebase
        .auth()
        .currentUser.updateProfile({
          displayName: this.username,
        })
        .then(() => {
          console.log("Up date Profile");
        });
      await firebase.auth().currentUser.providerData.forEach(function(profile) {
        console.log("  Provider-specific UID: " + profile.uid);
        console.log("  Name: " + profile.displayName);
        console.log("  Email: " + profile.email);
      });
    },
  },
};
</script>
<style lang=""></style>
