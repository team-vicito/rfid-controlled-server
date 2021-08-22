const socketio = require("socket.io");
const express = require("express");
const http = require("http");
const app = express();

const server = http.createServer(app);
const socket = new socketio.Server(server);
const port = 1337;

let conn;

const emitPostData = (data) => {
  if (conn) conn.emit("rfid", data);
}

app.use(express.urlencoded({extended: true}));

app.get("/", (_, res) => {
  res.sendFile(__dirname + "/public/index.html");
});

app.post("/post", (req, res) => {
  emitPostData(req.body.data);

  res.sendStatus(200);
});

socket.on("connection", (connection) => {
  conn = connection;

  connection.on('disconnect', () => {
    conn = null;
  });
});

server.listen(port, () => {
  console.log(`Success! Your application is running on port ${port}.`);
});
