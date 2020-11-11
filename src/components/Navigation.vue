<template>
    <div id="navi">
        <el-menu :default-active="activeIndex" @select="handleSelect" class="el-menu-demo" mode="horizontal">
            <el-menu-item index="1">情感分析</el-menu-item>
            <el-submenu index="2">
                <template slot="title">算法选择</template>
                <el-menu-item index="2-1">选项1</el-menu-item>
                <el-menu-item index="2-2">选项2</el-menu-item>
                <el-menu-item index="2-3">选项3</el-menu-item>
                <el-submenu index="2-4">
                    <template slot="title">选项4</template>
                    <el-menu-item index="2-4-1">选项1</el-menu-item>
                    <el-menu-item index="2-4-2">选项2</el-menu-item>
                    <el-menu-item index="2-4-3">选项3</el-menu-item>
                </el-submenu>
            </el-submenu>
        </el-menu>
    </div>
</template>

<script>
    export default {
        name: "Navigation"
    }
</script>

<style scoped>
#navi{

}
</style>