//需要连接的mysql的配置语句
const mysql = require("mysql");

class db {
    getConn(){
        let conn = mysql.createConnection({
            host: '127.0.0.1',
            user: 'root',
            password: '123456',
            database: 'yanyan',
            port: '3306'
        });
        conn.connect();
        return conn;
    }
}
module.exports = db;
