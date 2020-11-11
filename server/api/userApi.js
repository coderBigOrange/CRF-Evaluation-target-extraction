const express = require('express');
const router = express.Router();
const j = require('j')
const cmd = require('node-cmd')
const async = require('async')
const sql = require('../sql');
const DBHelper = require('../db');
const fs = require('fs')
const path = require('path')

const jsonWrite = function(res,ret){
    if(typeof ret === "undefined"){
        res.json({
            code:1,
            msg:"failed"
        })
    } else {
        res.json(
            ret
        )
    }
}

router.post('/insertData',(req,res)=>{
    let sqlStr = sql.user.insertData;
    let params = req.body;
    let db = new DBHelper();
    let conn = db.getConn();
    conn.query(sqlStr,
        [params.comment,params.goods_info,params.transport_info,params.service_info,params.reality],
        (err,result)=>{
            if(err) {
                res.json(err);
            } else {
                jsonWrite(res,result)
            }
        });
    conn.end();
});

router.post('/getData',(req,res)=>{
    let sqlStr = sql.user.getRates;
    let params = req.body;
    let conn = new DBHelper().getConn();
    console.log(params);
    conn.query(sqlStr,[params.comments],(err,result)=>{
        if(err){
            res.json(err);
        } else{
            jsonWrite(res,result)
        }
    });
    conn.end();
});

router.post('/addUser', (req, res) => {
    let sqlStr = sql.user.addUser
    let params = req.body;
    console.log(params);
    let conn = new DBHelper().getConn();
    conn.query(sqlStr, [params.name, params.age], (err, result) => {
        if (err) {
            res.json(err);
        } else {
            jsonWrite(res,result)
        }
    });
    conn.end();
});

router.post('/getUser', (req, res) => {
    let sqlStr = sql.user.getUser;
    let conn = new DBHelper().getConn();
    conn.query(sqlStr,function(err, result){
        if (err) {
            res.json(err);
        } else {
            jsonWrite(res,result)
        }
    });
    conn.end();
});

router.post('/mkdir',(req)=>{

    let param = req.body;
    console.log(param);
    const folder = "file/";
    //文件夹名称

    const name =  "sentiment"//文件名
    const suffix = "txt"//文件格式
    const fullName = folder + name + '.' + suffix//文件全名
    const content = param.input//文件内容

    const file = path.join(__dirname, fullName);

    fs.writeFile(file,content,function (err) {
        if(err){
            return console.error(err);
        }
        console.log("文件创立成功")
    })

});

//读预测文件
router.post('/readFile',(res)=>{

    const fullName = "\\file\\predict.xls";
    const loc = __dirname+fullName;
    console.log(loc);
    let data = j.readFile(loc,{});
    let j_data = j.utils.to_json(data);
    console.log(j_data);
    res.json(j_data);
})

router.post('/getModelData',(req,res)=>{
    console.log("in analyse")
    const param = req.body;

    const folder = "file/";
    //文件夹名称

    const name =  "sentiment"//文件名
    const suffix = "txt"//文件格式
    const fullName = folder + name + '.' + suffix//文件全名
    const content = param.input//文件内容
    const file = path.join(__dirname, fullName);

    fs.writeFile(file,content,'utf-8',(err)=>{
        if(err) console.log(err);
        else {
            console.log("写入成功");
        }
    });

    cmd.run("python D:\\vue-projects\\segment_v1.0\\server\\api\\file\\label.py");
    cmd.run("crf_test -m res_m D:\\vue-projects\\segment_v1.0\\server\\api\\file\\res_label.data >> output");

    fs.readFile('D:\\vue-projects\\segment_v1.0\\output','utf-8',function(err,data){
       if(err){
           console.log(err);
           return;
       }else {
           console.log(data)
           res.json({
               output:data
           })
           fs.writeFile("D:\\vue-projects\\segment_v1.0\\output","",'utf-8',(err)=>{
               if(err) console.log(err);
               else {
                   console.log("清除成功");
               }
           });
       }
    });



})

module.exports = router;
