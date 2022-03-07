const app = require("./app")
const dotenv = require("dotenv")
const connectDatabase = require("./config/database")
const cloudinary = require("cloudinary")
dotenv.config({ path: "api/config/.env" })



connectDatabase()

cloudinary.config({
    cloud_name: process.env.CLOUDINARY_NAME,
    api_key: process.env.CLOUDINARY_API_KEY,
    api_secret: process.env.CLOUDINARY_API_SECRET,
})



app.get("/", (req, res) => {
    res.send("hello world")
})


app.listen(`${process.env.PORT}`, () => {
    console.log(`working on the port ${process.env.PORT}`)
})