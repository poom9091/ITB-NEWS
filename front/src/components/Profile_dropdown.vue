<template lang="">
    <div class="relative">
        <button v-on:click="isOpen=!isOpen" class="focus:outline-none  block transition duration-300 ease-in-out p-2  rounded-full 
                        bg-white text-blue-500  sm:border-4 border-blue-600
                        hover:bg-blue-400 hover:text-white " >
            <svg xmlns="http://www.w3.org/2000/svg" class=" sm:h-6 sm:w-6 w-4 h-4 " viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd" />
            </svg>
        </button>
        <button v-if="isOpen" @click="isOpen=false" class="fixed top-0 right-0 bottom-0 left-0 h-full w-full " ></button>
        <div v-if="isOpen" class=" absolute right-0 mt-2 py-3  w-44 bg-white rounded-md shadow-xl space-y-2">
            <a href="#" @click="go_profile(user.uid,user.name)" class="block text-gray-900 text-base hover:bg-blue-600 px-4 py-2 hover:text-white">{{ user.name }}</a >
            <a href="#" @click="logout()" class="block text-gray-900 text-base hover:bg-blue-600 px-4 py-2 hover:text-white">Sign out</a>
        </div>
    </div>
</template>
<script>
import { mapGetters,mapActions } from "vuex";
export default {
    data() {
        return {
            user:'',
            isOpen:false
        }
    },
    methods: {
        ...mapActions(['Logout']),
        ...mapGetters(['getUID']),
        logout(){
            this.Logout()
            localStorage.removeItem('uid');
            localStorage.removeItem('name');
            this.$router.push("/");
        },
        go_profile(uid,name){
            // this.$router.push("/board/profile/"+uid);
            this.isOpen = false
            this.$router.push(({ path: `/board/profile/${uid}/${name}` }))
        }
    },
    created() {
        this.user = this.getUID()
    },
}
</script>
<style lang="">
    
</style>