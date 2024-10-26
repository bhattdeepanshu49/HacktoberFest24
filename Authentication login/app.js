const express = require('express');
const cookieParser = require('cookie-parser');
const bcrypt = require('bcrypt'); // Assuming you'll use bcrypt later for user authentication
var jwt = require('jsonwebtoken');
const app = express();
app.use(cookieParser()); // Enable cookie parsing

// Generate a JWT token (place it in a login or authentication route)
function generateToken(email) {
  return jwt.sign({ email }, "secret"); // Replace "secret" with a strong secret key
}

// Route to handle login or authentication (replace with your login logic)
app.post("/login", async (req, res) => {
  // Validate user credentials (replace with actual authentication)
  const isValid = true; // Replace with your validation logic

  if (isValid) {
    const token = generateToken(req.body.email); // Generate token if login is successful
    res.cookie('token', token, { httpOnly: true }); // Set the token cookie with HttpOnly flag
    res.send("Login successful");
  } else {
    res.status(401).send("Invalid login credentials"); // Send unauthorized response
  }
});

// Route to read data
app.get("/read", (req, res) => {
  const token = req.cookies.token;

  if (!token) {
    return res.status(401).send("Unauthorized: No JWT token provided"); // Handle missing token
  }

  try {
    const data = jwt.verify(token, "secret");
    console.log(data);
    res.send("Decoded data");
  } catch (error) {
    if (error.name === 'JsonWebTokenError') {
      return res.status(401).send("Unauthorized: Invalid JWT token"); // Handle invalid token
    } else {
      console.error(error); // Log other errors
      res.status(500).send("Internal Server Error"); // Generic error for unexpected issues
    }
  }
});

app.listen(3004, function() {
  console.log('Server started on port 3004');
});


