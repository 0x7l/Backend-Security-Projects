const express = require("express");
const router = express.Router();
const userRoutes = require("./routes/userRoutes");

// Add routes here
router.use("/users", userRoutes);

// Example base route
router.get("/Welcome", (req, res) => {
  res.send("Welcome to the API!");
});

module.exports = router;
