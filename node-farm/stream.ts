const fs = require("fs");
const server = require("http").createServer();

server.on("request", (req, res) => {
  const readable = fs.createReadStream("try2.txt");
  let wstream = fs.createWriteStream(
    "C:\\Users\\CEO\\Desktop\\node-farm\\try.txt"
  );
  readable.on("data", (x) => {
    wstream.write(x);
  });
});

server.listen(3000, "127.0.0.1", () => {
  console.log(`listening on 3000`);
});
