<template>
<div>
    <div class="flex bg-blue-500 p-4 text-white justify-between ">
        <div class=" font-extrabold text-3xl">
            
            <h1>ITB-NEWS</h1>
        </div>
        <div class="flex space-x-4 text-xl font-semibold ">
            <router-link class="transition duration-300 ease-in-out p-2 rounded-xl 
                        hover:bg-white hover:text-blue-500 hover:text-2xl"
                        to="/">
                        Board</router-link> 
            <router-link class="transition duration-300 ease-in-out p-2 rounded-xl 
                        hover:bg-white hover:text-blue-500 hover:text-2xl"
                        to="/news">News Today</router-link>
            <!-- <button class="transition duration-300 ease-in-out p-2 rounded-xl 
                        hover:bg-white hover:text-blue-500 hover:text-2xl">
                    Board
            </button>
            <button class="transition duration-300 ease-in-out p-2 hover:bg-white hover:text-blue-500 rounded-xl">News Today</button> -->
        </div>
        <!-- </div>
        <div>
            <h1</h1>
        </div> -->
    </div>
</div>
</template>

<script>
export default {
    name:'Navbar'
}
</script>

<style>

</style>