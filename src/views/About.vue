<template>
    <div id="about">
        <div style="margin-bottom: 30px">
            <navigation></navigation>
        </div>
        <div id="container">
            <div id="div1">
                <el-container>
                    <el-header>输入数据</el-header>
                    <el-input :rows="6" class="el-main" type="textarea" v-model="inputData"/>
                </el-container>
            </div>
            <div id="div2">
                <el-container>
                    <el-header>输出结果</el-header>
                    <textarea class="el-main" v-model="transform" readonly></textarea>
                </el-container>
            </div>
        </div>
        <hr :style="style1">
        <el-button @click="mkdir" :style="style4">点击获取</el-button>
        <p></p>
    </div>
</template>
<script>
    import Navigation from "../components/Navigation";
    import axios from 'axios'

    export default {
        name: "about",
        components: {Navigation},
        data() {
            return {
                style1: {
                    marginTop: '30px',
                    marginBottom: '30px',
                    color: '#99A9BF'
                },
                style2:{
                    marginLeft:'60px'
                },
                style3:{
                    fontsize:"30px"
                },
                style4:{
                    background:"cornflowerblue",
                    float:'right',
                    marginRight:'150px',
                    color:"white",
                },
                colors: ['#99A9BF', '#F7BA2A', '#FF9900'],
                inputData:"",
                outputData:{
                    noun:[],
                    adj:[]
                },
                userName:"",
                age:"",
                analyseData:""
            }
        },
        methods: {
            addUser() { //添加用户
                let name = this.userName;
                let age = this.age;
                axios.post('/api/user/addUser', {
                    name,
                    age
                }).then(res => {
                    alert('信息添加成功');
                    this.outputData = res.data;
                    console.log(res,toString());
                }).catch(err => {
                    console.log(err)
                })
            },
            getUser() { //添加用户
                axios.post('/api/user/getUser').then(res => {
                    alert('信息查询成功');
                    this.outputData = res.data;
                    console.log(res.toString());
                }).catch(err => {
                    console.log(err)
                })
            },
            mkdir(){
                //创建文本文件
                const input = this.inputData;
                axios.post('/api/user/getModelData',{
                    input
                }).then(res=> {
                    let noun = [];
                    let adj = [];
                    let sentenceArr = res.data.output.split("\r\n");
                    let wordArr = [];
                    for(let i=0;i<(sentenceArr.length-2);i++){
                        let temp = sentenceArr[i].split("\t");
                        wordArr.push(temp);
                    }
                    for(let i=0;i<wordArr.length;i++){
                        if(wordArr[i][1]==="NN"){
                            noun.push(wordArr[i][0]);
                        }
                        if(wordArr[i][1]==="JJ"){
                            adj.push(wordArr[i][0]);
                        }
                    }
                    this.outputData.noun = noun;
                    this.outputData.adj = adj;
                    console.log(wordArr);
                    console.log(sentenceArr);
                }).catch(err=>{
                    console.log(err)
                })
            },
            readFile(){
                axios.post('/api/user/readFile').then(res=>{
                    console.log(res.data);
                }).catch(err=>{
                    console.log(err);
                })
            }
        },
        computed:{
            transform:{
                get(){
                    let data = [];
                    for(let i=0;i<this.outputData.adj.length;i++){
                        let temp = this.outputData.noun[i]+':'+this.outputData.adj[i];
                        data.push(temp);
                    }
                    return data.join('\n');
                }
            }
        }
    }
</script>

<style scoped>
    #div1 {
        display: inline-block;
        width: 40%;
        margin-right: 60px;
    }

    #div2 {
        display: inline-block;
        width: 40%;
        margin-left: 60px;
    }

    #about{
        margin-bottom: 60px;
    }
    .el-header, .el-footer {
        background-color: #B3C0D1;
        color: #333;
        text-align: center;
        line-height: 60px;
    }
    .el-main {
        background-color: #E9EEF3;
        color: #333;
        font-size: large;
        text-align: left;
        height: 200px;
    }
    #types {
        float: left;
    }

    #rate {
        float: left;
        margin-left: 10px;
    }
</style>