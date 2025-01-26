const mongoose = require("mongoose");
const path = require("path");
require("dotenv").config({path : "config/.env"});

const connect = async () => {
  try {
    const DB_URI = process.env.DB_URI || "mongodb://localhost:27017/mydatabase";
    await mongoose.connect(DB_URI, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log("Connected to the database successfully.");
  } catch (error) {
    console.error("Failed to connect to the database:", error.message);
    process.exit(1); // Exit the application if the database connection fails
  }
};

module.exports = { connect };
