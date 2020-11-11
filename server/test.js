const cmd = require('node-cmd')

function f() {
    // const param = "python label.y";
    cmd.run("crf_test -m res_m D:\\vue-projects\\segment_v1.0\\server\\api\\file\\res_label.data >> output")
}

f();