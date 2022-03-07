const mongoose = require("mongoose")

const connectDatabase = () => {
    mongoose.connect("mongodb://localhost:27017/signin", { useNewUrlParser: true, useUnifiedTopology: true, useCreateIndex: true })
        .then(() => {
            console.log("database is connected")
        }).catch((err) => {
            console.log(err)
        })
}


module.exports = connectDatabase