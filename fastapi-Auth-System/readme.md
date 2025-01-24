# FastAPI User Authentication System

A robust and scalable user authentication system built using FastAPI, SQLAlchemy, and MySQL. This project demonstrates essential functionalities such as user signup, user login, and retrieving user details after successful login.

---

## Features

### User Signup
- Allows users to register with the following details:
  - `username`
  - `password`
  - `email`
  - `mobile`
  - `date of birth`
  - `name`
  - `location`
  - `father’s name`
- Validates the input fields to ensure data integrity.
- Stores user details securely in a MySQL database.

### User Login
- Enables users to log in using their username and password.
- Validates credentials against the database.
- Provides a success response if credentials are correct or an error if they are invalid.

### Retrieve User Details
- After a successful login, displays the user information provided during signup.

### SQLAlchemy ORM
- Leverages SQLAlchemy for efficient interaction with the MySQL database.

### Secure Practices
- Input validation using Pydantic.
- Code designed to prevent SQL injection by relying on ORM methods.

---

## Endpoints

### 1. Signup
**URL:** `/signup`  
**Method:** `POST`  
**Query Parameters:**
- `username` (string) - Required
- `password` (string) - Required
- `email` (string) - Required
- `mobile` (integer) - Required
- `dob` (string) - Required
- `name` (string) - Required
- `location` (string) - Required
- `fathername` (string) - Required  

**Response:**
- `200`: Signup successful.
- `422`: Validation error.

---

### 2. Login
**URL:** `/login`  
**Method:** `POST`  
**Request Body:**
```json
{
  "username": "your_username",
  "password": "your_password"
}

Response:

    200: Login successful, returns the username.
    401: Invalid credentials.
    422: Validation error.

3. Get User Details

URL: /details
Method: GET
Response:

    Returns all user details submitted during signup.

Installation
Prerequisites

    Python 3.9+
    MySQL Server

Setup Instructions

    Clone the repository:

git clone https://github.com/your-username/fastapi-auth-system.git
cd fastapi-auth-system

Install dependencies:

pip install -r requirements.txt

Configure the database:

    Update the DATABASE_URL in the code:

    DATABASE_URL = "mysql+pymysql://<username>:<password>@<host>/<database_name>"

Apply database migrations:

python main.py

Run the FastAPI server:

    uvicorn main:app --reload

    Access the API documentation at:
        Swagger UI: http://127.0.0.1:8000/docs
        ReDoc: http://127.0.0.1:8000/redoc

Folder Structure

fastapi-auth-system/
├── main.py          # Entry point of the application
├── models.py        # SQLAlchemy models
├── schemas.py       # Pydantic schemas for validation
├── database.py      # Database setup and session configuration
├── requirements.txt # Python dependencies
└── README.md        # Project description and documentation

Future Enhancements

    Implement password hashing for secure storage using bcrypt or argon2.
    Add JWT-based authentication for token management.
    Add role-based access control (RBAC).
    Implement email verification during signup.
    Add rate-limiting to prevent brute-force attacks on login.

Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
License

This project is licensed under the MIT License.
