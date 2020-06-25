const express = require('express')
const app = express();
app.use(express.static('files'))
var fs = require("fs")
// Parse URL-encoded bodies (as sent by HTML forms)
app.use(express.urlencoded());

// Parse JSON bodies (as sent by API clients)
app.use(express.json());

app.get('/', (req, res) => {
  res.sendFile("index.html")
});

app.listen(80, () => {
  
});

app.post("/saveshop", (req, res)=> {
  fs.writeFile("files/shops.json", req.body.file, "utf-8", function(err){
    if(err){
      console.log("bummer")
    } else {
      console.log("cool")
    }
  })
  
})
//module.exports = app;
