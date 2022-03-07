const User = require("../models/userModel")
const cloudinary = require("cloudinary")


exports.registerUser = async (req, res) => {
    try {

        const myCloud = await cloudinary.v2.uploader.upload(req.body.avatar, {
            folders: "avatar",
            width: 150,
            crop: "scale",

        })
        const { name, email, password } = req.body

        const user = await User.create({
            name,
            email,
            password,
            avatar: {
                public_id: myCloud.public_id,
                url: myCloud.secure_url,
            }
        })
        console.log(user)

        res.status(200).json({
            success: true,
            user
        })
    } catch (err) {
        res.status(500).json(err)
    }
}