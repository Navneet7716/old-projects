var fs = require("fs");
var http = require("http");
var url = require("url");

const server = http.createServer((req, res) => {
  res.writeHead(200, { "Content-Type": "text/html" });

  var url = req.url;

  if (url === "/about") {
    const readable = fs.createReadStream("student.html");
    readable.pipe(res);
  } else if (url === "/contact") {
    const readable = fs.createReadStream("try3.txt");
    readable.pipe(res);
  } else {
    res.write("Hello World!");

    res.end();
  }
});
server.listen(8000, "127.0.0.1", function () {
  console.log("listening on 8000");
});
