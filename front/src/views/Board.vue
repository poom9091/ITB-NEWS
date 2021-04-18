<template>

  <div class=" max-w-max w-8/12 mx-auto py-4 my-24  bg-gray-200" >
      <!-- <div class=" text-4xl font-bold text-blue-500">Board</div> -->
      <router-view class="flex flex-col space-y-2 px-3"/>
      
  </div>
</template>

<script>
// import post from '../components/all_post'
// import post_by_profile from '../components/all_post_profile'
export default {
  data() {
    return {
      profile:this.$route.params.name
    }
  },
  mounted() {
    console.log(this.profile)
  },
  components:{
    // post,
    // post_by_profile
  }
}
</script>

<style>

</style>