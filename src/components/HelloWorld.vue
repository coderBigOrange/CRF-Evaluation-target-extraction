<template>
  <el-carousel height="800px" direction="vertical" :autoplay="true">
    <el-carousel-item v-for="(item,index) in img" :key="index">
      <img :src="item.url" alt="找不到图片" height="600"/>
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
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
</style>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data(){
    return {
        img:[
          {url:require('../../src/assets/teach1-zoom.png')},
          {url:require('../../src/assets/teach2-zoom.png')},
           {url:require('../../src/assets/teach3-zoom.png')}
        ]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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
