const fs = require("fs");
const http = require("http");
const url = require("url");

server.on("request", (req, res) => {
  const { query, pathname } = url.parse(req.url, true);
  const pathName = req.url;
  if (pathName === "/student") {
    const readable = fs.createReadStream("student.txt");
    readable.pipe(res);
  } else if (pathName === "/try") {
    const readable = fs.createReadStream("try3.txt");
    readable.pipe(res);
  }
});

server.listen(8000, "127.0.0.1", () => {
  console.log("listening on 8000");
});
