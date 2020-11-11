<template>
    <el-row>
        <el-button type="primary" round @click="show">分    析</el-button>
    </el-row>
</template>

<script>
    export default {
        name: "transportButton",
        methods:{
            show(event){
                console.log(event)
            }
        }
    }
</script>

<style scoped>

</style>