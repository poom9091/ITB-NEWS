<template>
    <div class=" h-screen bg-gray-300 py-14">
        <div class="bg-white rounded-md  max-w-2xl mx-auto p-6">
            <div class=" text-3xl font-semibold text-blue-400">Create Post</div>
            <div class="flex flex-col space-y-4">
                <div>{{$route.params.title}}</div>
                <div>{{$route.params.description}}</div>
                <img :src="$route.params.img" class="rounded-xl w-4/12 " >
                <input id='title' class=" bg-gray-200 rounded-sm p-3 text-black" placeholder="Title">
                <input class=" bg-gray-200 rounded-sm">
            </div>
            
        </div>
        <div>
            
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style>

</style>