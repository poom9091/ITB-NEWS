<template>
  
    <div class=" flex flex-wrap mt-28">
      <div
        class=" mx-auto  px-5 py-6 rounded-lg flex flex-col relative border-blue-900 border-4 w-96 space-y-4"
      > 
        <router-view/>
        <!-- <tem_login/> -->
      </div>
    </div>
</template>

<script>
import { mapState } from "vuex";
// import tem_login from '../components/template_login';
// import VFacebookLogin from 'vue-facebook-login-component'
export default {
  mounted() {
    if(this.user.uid != null){
      console.log(this.user.uid.length);
      this.$router.push("/");
    }
  },
  computed: {
    ...mapState(["user"]),
  },
};
</script>

<style></style>
