const express = require("express")
const session = require('express-session')
const axios = require('axios')
const app = express() 
const download = require('download');
const fs = require("fs");
const https = require("https");
const got = require("got");
const { createWriteStream } = require("fs");
const { DownloaderHelper } = require("node-downloader-helper");

app.use(express.json({
    type: 'application/json',
  }))
      
// Port Number Setup
var PORT = process.env.port || 3000
   
// Session Setup
app.use(session({
  
    // It holds the secret key for session
    secret: 'Your_Secret_Key',
  
    // Forces the session to be saved
    // back to the session store
    resave: true,
  
    // Forces a session that is "uninitialized"
    // to be saved to the store
    saveUninitialized: true
}))

app.post("/", async (req,res) => {
    const myarr =[]
    const {data} = req.body
    // console.log(data)
    if(data){
        if(data && data.gfyItem){

            myarr.push(data.gfyItem.content_urls.mp4.url)
        }
        else{
            
        }
        // console.log("here")
        // console.log(data.gfyItem.content_urls.mp4.url)
        // res.json(data.data.gfyItem.content_urls.mp4.url)
    }
    else{
        // console.log("there")
        // console.log(data.gif.urls.hd)
        if(data && data.gif){

            myarr.push(data.gif.urls.hd)
        }
        else{
            return
        }

    }
        
    return res.json(myarr[0])
})

app.get("/download", function(req, res){
    // var name = req.session.name
    // return res.send(name)

const url = "https://media0.giphy.com/media/4SS0kfzRqfBf2/giphy.gif";
const fileName = "image.gif";

const downloadStream = got.stream(url);
const fileWriterStream = createWriteStream(fileName);

downloadStream
  .on("downloadProgress", ({ transferred, total, percent }) => {
    const percentage = Math.round(percent * 100);
    console.error(`progress: ${transferred}/${total} (${percentage}%)`);
  })
  .on("error", (error) => {
    console.error(`Download failed: ${error.message}`);
  });

fileWriterStream
  .on("error", (error) => {
    console.error(`Could not write file to system: ${error.message}`);
  })
  .on("finish", () => {
    console.log(`File downloaded to ${fileName}`);
  });

downloadStream.pipe(fileWriterStream);

})


app.get("/", function(req, res){

    // req.session.key = value
    req.session.name = 'GeeksforGeeks'
    return res.send("Session Set")
})
   
app.get("/session", async function(req, res){
    const myarr = []
    var name = req.session.name
    
    const config = {
        method: 'get',
        url: "https://api.redgifs.com/v1/gifs/thunderouswoodencamel",
        headers: {
            'Content-Type': 'application/json',
          }
        
    }
    const data = await axios(config)
    if(data.data && data.data.gfyItem){
        // console.log("here")
        // console.log(data.gfyItem.content_urls.mp4.url)
        myarr.push(data.data.gfyItem.content_urls.mp4.url)
        // res.json(data.data.gfyItem.content_urls.mp4.url)
    }
    else{
        // console.log("there")
        // console.log(data.gif.urls.hd)
    myarr.push(data.data.gif.urls.hd)
    }

    

// req.session.destroy(function(error){
    //     console.log("Session Destroyed")
    // })
})

app.get("/final", async function(req, res)  {
    const myarr =[]
    const config = {
        method: 'get',
        url: "https://api.redgifs.com/v1/gifs/firstanimatedlionfish",
        headers: {
            'Content-Type': 'application/json',
             
          },
                  
    }
    const data = await axios(config)

    if(data.data && data.data.gfyItem){
        // console.log("here")
        // console.log(data.gfyItem.content_urls.mp4.url)
        myarr.push(data.data.gfyItem.content_urls.mp4.url)
        // res.json(data.data.gfyItem.content_urls.mp4.url)
    }
    else{
        // console.log("there")
        // console.log(data.gif.urls.hd)
    myarr.push(data.data.gif.urls.hd)
    }
          
})
    
app.listen(PORT, function(error) {
    console.log("Server created Successfully on PORT :", PORT)
})
