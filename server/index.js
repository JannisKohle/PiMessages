const express = require("express");
const app = express();

app.use(express.json());

app.listen(7777, () => console.log("Server listening on port 7777"));
