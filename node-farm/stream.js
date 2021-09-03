var fs = require("fs");
var server = require("http").createServer();
server.on("request", function (req, res) {
    var readable = fs.createReadStream("try2.txt");
    var wstream = fs.createWriteStream("C:\\Users\\CEO\\Desktop\\node-farm\\try.txt");
    readable.on("data", function (x) {
        wstream.write(x);
    });
});
server.listen(3000, "127.0.0.1", function () {
    console.log("listening on 3000");
});
