<template>
    <el-input
            type="textarea"
            :rows="8"
            v-model="textarea">
    </el-input>
</template>

<script>
    export default {
        data() {
            return {
                textarea: ''
            }
        }
    }
</script>

<style scoped>

</style>