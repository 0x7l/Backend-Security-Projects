const jwt = require("jsonwebtoken");

const generateToken = (user) => {
  const payload = {
    id: user._id,
    email: user.email,
  };

  const token = jwt.sign(payload, process.env.JWT_SECRET || "defaultSecret", {
    expiresIn: "1h", // Token expires in 1 hour
  });

  return token;
};

module.exports = { generateToken };
