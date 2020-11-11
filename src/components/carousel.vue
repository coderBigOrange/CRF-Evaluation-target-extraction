<template>
    <el-carousel :autoplay="true" type="card" height="400px" indicator-position="outside">
        <el-carousel-item :key="item" v-for="item in 3">
            <h3 class="medium">{{ item }}</h3>
        </el-carousel-item>
    </el-carousel>
</template>
<style>
    .el-carousel__item h3 {
        color: #475669;
        font-size: 30px;
        opacity: 0.75;
        line-height: 200px;
        margin: 0;
    }

    .el-carousel__item:nth-child(2n) {
        background-color: #99a9bf;
        img-sour
    }

    .el-carousel__item:nth-child(2n+1) {
        background-color: #d3dce6;
    }
</style>
<script>
    export default {
        name: "carousel"
    }
</script>

<style scoped>
    h3 {
        margin: 40px 0 0;
    }
    ul {
        list-style-type: none;
        padding: 0;
    }
    li {
        display: inline-block;
        margin: 0 10px;
    }
    a {
        color: #42b983;
    }
</style>