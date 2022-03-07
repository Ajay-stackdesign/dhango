const mongoose = require("mongoose");
const validator = require("validator")
const bcrypt = require("bcryptjs")

const userSchema = new mongoose.Schema({
    name: {
        type: String,
        required: [true, "Please enter the Number"],
        maxLength: [4, "Name should be more than 4 charcater"]
    },
    email: {
        type: String,
        required: [true, "Please Enter the Email"],
        unique: true,
        validate: [validator.isEmail, "Please enter the valid email"]
    },
    password: {
        type: String,
        required: [true, "Please enter the Password"],
        minLength: [8, "password should be more than 8 character"],
        select: false
    },
    avatar: {
        public_id: {
            type: String,
            required: true
        },
        url: {
            type: String,
            required: true
        }
    },
    createdAt: {
        type: Date,
        default: Date.now
    }
})

userSchema.pre("save", async function (next) {
    if (!this.isModified("password")) {
        next()
    }
    this.password = await bcrypt.hash(this.password, 10)
})

module.exports = new mongoose.model("User", userSchema)