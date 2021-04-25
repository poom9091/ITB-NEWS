<template lang="">
     <div class="px-2 lg:px-20 py-10  ">
        <div
        class=" flex justify-between  px-4 pb-5 border-b-4 border-dashed border-blue-400 "
        >
        <div class="text-4xl  text-blue-600 font-extrabold">Post</div>
        <sort_data/>
        </div>
        
        <post class="space-y-3 py-3 px-3" />
        
    </div>
</template>
<script>
import sort_data from '../components/sort_post'
import post from '../components/Posted/all_post'
export default {
    components:{
        post,
        sort_data
    }
}
</script>
<style lang="">
    
</style>