import express from "express";
import mongoose from "mongoose";

const app = express();

app.get("/", (req, res)=> {

	
res.send("hello world");

}); 

app.listen(3000, () => console.log("Running on Port 3000"));



