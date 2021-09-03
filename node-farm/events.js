const EventEmitter = require("events");
const http = require("http");

class Sales extends EventEmitter {
  constructor() {
    super();
  }
}

const myEmitter = new Sales();

myEmitter.on("newSale", () => {
  console.log("There was a New sale");
});

myEmitter.on("newSale", () => {
  console.log("Customer name jonas");
});

myEmitter.on("newSale", (stock) => {
  console.log(`There are Now ${stock} items left in stock`);
});

myEmitter.emit("newSale", 9);

const server = http.createServer();

server.on("request", (req, res) => {
  console.log("request Recieved");
  res.end("request Recieved");
});

server.on("request", (req, res) => {
  console.log("request Recieved 😬");
});

server.on("close", () => {
  res.end("server closed");
});

server.listen(8000, "127.0.0.1", () => console.log("waiting for request"));
