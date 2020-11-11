
//node 后端服务器
const http = require('http')
const userApi = require('./api/userApi');
const bodyParser = require('body-parser');
const express = require('express');//引入express


let app = express();
let server = http.createServer(app);

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
    extended: false
}));

//后端api路由
app.use('/api/user', userApi);

//监听端口
server.listen(3000,()=>{
    console.log('success listen at port :3000......')
});

