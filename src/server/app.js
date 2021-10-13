const socketio = require("socket.io");
const express = require("express");
const http = require("http");
const app = express();

const server = http.createServer(app);
const socket = new socketio.Server(server);
const port = 1337;

let conn;
const path = `${__dirname}/public/interactive-model-viewer`;

const emitPostData = (data) => {
  if (conn) conn.emit("rfid", data);
}

app.use(express.urlencoded({extended: true}));
app.use("/", express.static(`${path}/public/`));
app.use("/dist", express.static(`${path}/dist/`));

app.get("/", (_, res) => {
  res.sendFile(`${path}/index.html`);
});

app.post("/post", (req, res) => {
  console.log("Data recieved");
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
  console.log(`Web server active. Listening on port ${port}.`);
});
