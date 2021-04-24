<template lang="">
     <div class="relative text-xs sm:text-base">
        <button v-on:click="isOpen=!isOpen" class="focus:outline-none  block transition duration-300 ease-in-out p-2  rounded-xl 
                        bg-white text-blue-500 border-2 border-blue-600 shadow-lg 
                        hover:bg-blue-600 hover:text-white " >
           {{ sort_msg }}
        </button>
        <button v-if="isOpen" @click="isOpen=false" class="fixed top-0 right-0 bottom-0 left-0 h-full w-full " ></button>
        <div v-if="isOpen" class=" absolute  right-0  mt-3 py-3  w-44 bg-white rounded-md shadow-xl space-y-2 border-2 border-blue-900 z-50">
            <a  @click="Sort_time()" class="cursor-pointer block text-gray-900 text-base hover:bg-blue-600 px-4 py-2 hover:text-white">Sort by Time</a>
            <a  @click="Sort_view()" class="cursor-pointer block text-gray-900 text-base hover:bg-blue-600 px-4 py-2 hover:text-white">Sort by View</a>
            <a  @click="Sort_vote()" class="cursor-pointer block text-gray-900 text-base hover:bg-blue-600 px-4 py-2 hover:text-white">Sort by Vote</a>
            <a  @click="Sort_commnet()" class="cursor-pointer block text-gray-900 text-base hover:bg-blue-600 px-4 py-2 hover:text-white">Sort by Comment</a>
        </div>
    </div>
</template>
<script>
import { mapActions } from 'vuex'
export default {
    data() {
        return {
            user:'',
            isOpen:false,
            sort_msg:''
        }
    },
    created() {
        this.Sort_time()
    },
    methods: {
       ...mapActions(['getPostFromApi','Sort_View','Sort_Vote','Sort_Comment']),
       Sort_time(){
           this.getPostFromApi()
           this.isOpen=false
           this.sort_msg='Sort by Time'
       },
        async Sort_view(){
           await this.getPostFromApi()
           await this.Sort_View()
           this.isOpen=false
           this.sort_msg='Sort by View'
       },
       async Sort_vote(){
           await this.getPostFromApi()
           await this.Sort_Vote()
           this.isOpen=false
           this.sort_msg='Sort by Vote'
       },
       async Sort_commnet(){
           await this.getPostFromApi()
           await this.Sort_Comment()
           this.isOpen=false
           this.sort_msg='Sort by Comment'
       }
    },
}
</script>
<style lang="">
    
</style>