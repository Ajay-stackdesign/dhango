const express = require("express")

const app = express()
app.use(express.json())

const userRoute = require("./route/userRoute")

app.use("/api/v1", userRoute)

module.exports = app