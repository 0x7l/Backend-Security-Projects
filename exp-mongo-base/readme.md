# Express-Mongo Boilerplate

A lightweight and modular boilerplate for building APIs using Express.js and MongoDB. This project includes basic authentication, middleware setup, and routing, making it a great starting point for building secure Node.js applications.

## Features

- **Express.js**: Lightweight and fast web framework for Node.js.
- **MongoDB**: Database integration using Mongoose.
- **JWT Authentication**: Secure user authentication with JSON Web Tokens.
- **Modular Structure**: Organized folder structure for scalability.
- **Environment Variables**: `.env` file support using `dotenv`.

## Project Structure

```
├── app
│   ├── all_routes.js        # Central routing file
│   ├── controller
│   │   └── userController.js # Logic for user-related routes
│   ├── middleware
│   │   └── auth.js           # Authentication middleware
│   ├── model
│   │   └── schema.js         # Mongoose schema for users
│   ├── routes
│   │   └── userRoutes.js     # User routes
│   └── utils
│       └── tokenUtils.js     # Helper for generating JWT tokens
├── config
│   └── db.js                # MongoDB connection setup
├── package.json             # Project metadata and dependencies
├── server.js                # Entry point of the application
├── .env                     # Environment variables
└── README.md                # Project documentation
```

## Prerequisites

- [Node.js](https://nodejs.org/) (v14 or above)
- [MongoDB](https://www.mongodb.com/) (local or cloud-based)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/exp-mongo-base.git
   cd exp-mongo-base
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Create a `.env` file in the root directory and add the following:

   ```env
   DB_URI=mongodb://localhost:27017/mydatabase
   JWT_SECRET=your-secret-key
   PORT=5000
   ```

4. Start the server:

   ```bash
   npm run dev
   ```

   The server will run at `http://localhost:5000`.

## API Endpoints

### Public Routes
- `GET /api/users` - Retrieve all users
- `POST /api/users` - Create a new user

### Example Response

#### GET `/api/users`

```json
[
  {
    "_id": "64adccffafde8e4b9c8f58cd",
    "name": "John Doe",
    "email": "john@example.com",
    "password": "hashedpassword",
    "createdAt": "2023-01-25T10:30:00.000Z",
    "updatedAt": "2023-01-25T10:30:00.000Z"
  }
]
```

## Scripts

- `npm start` - Start the server in production mode
- `npm run dev` - Start the server in development mode with live reload using `nodemon`

## Technologies Used

- [Express.js](https://expressjs.com/)
- [Mongoose](https://mongoosejs.com/)
- [JWT](https://jwt.io/)
- [Nodemon](https://nodemon.io/)

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
