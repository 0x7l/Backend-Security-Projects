const express = require("express");
const router = express.Router();
const { getAllUsers, createUser } = require("../controller/userController");
const authMiddleware = require("../middleware/auth");

// Route to get all users
router.get("/M1", authMiddleware, getAllUsers);

// Route to create a new user
router.post("/", createUser);
router.use("/database", database_routes)

module.exports = router;
