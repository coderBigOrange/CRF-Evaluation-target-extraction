var sqlMap = {
    user: {
        //获取所有参数

        //通过参数选取数值
        getRates: 'select * from rate where comments = ?',
        //插入新数据
        insertData: 'insert into rate values(?,?,?,?,?)',
        //test
        addUser: 'insert into user(name, age) values (?,?)',
        //test2
        getUser: 'select * from user',
    }
}
module.exports = sqlMap;
