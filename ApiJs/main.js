const express = require("express");
const cors = require("cors"); 
const app = express();

app.use(cors());

app.get("/", (req, res) => {
    res.status(200).send("OK");
});

app.get("/check", (req, res) => {
    Message = {
        "Instancia": "Instancia #1 - API #1",
        "Curso":"Seminario de Sistemas 1",
        "Estudiante":"Estudiante - <202006373>"
    }
    res.status(200).json(Message);
});

app.listen(3000, () => {
    console.log("Server is running on port 3000");
});