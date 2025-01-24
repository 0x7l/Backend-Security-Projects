# Backend Security Projects

A curated collection of backend-focused projects that emphasize secure coding practices, authentication mechanisms, and vulnerability mitigation strategies. This repository is designed for developers, cybersecurity enthusiasts, and students to explore and learn secure development methodologies.

---

## Projects Included

1. **Secure Login System**
   - **Description:** A secure login system using FastAPI and MySQL.
   - **Features:**
     - User authentication with username and password.
     - SQL Injection prevention.
     - Signup and login endpoints.
     - Data validation using Pydantic models.

2. **Authentication Hub**
   - **Description:** A project showcasing multiple authentication methods such as JWT, OAuth2, and Session-based authentication.
   - **Features:**
     - JWT token generation and validation.
     - Role-based access control.
     - Password hashing with secure algorithms.

3. **IDOR Lab**
   - **Description:** A lab to demonstrate Insecure Direct Object References (IDOR) vulnerabilities and how to secure them.
   - **Features:**
     - Demonstration of IDOR exploitation.
     - Implementation of secure authorization checks.

4. **Rate Limiting System**
   - **Description:** A project implementing rate limiting to prevent brute force attacks.
   - **Features:**
     - Request throttling.
     - IP-based rate limiting.
     - Customizable rate-limiting rules.

---

## Getting Started

### Prerequisites

- Python 3.8+
- MySQL database
- Virtual environment tools (optional but recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/backend-security-projects.git
   cd backend-security-projects
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   - Create a MySQL database (e.g., `backend_security`).
   - Update the `DATABASE_URL` in the project files with your MySQL credentials.

5. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

### Testing

Use tools like Postman or cURL to test the endpoints provided in each project.

---

## Contribution

Contributions are welcome! If you'd like to contribute:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add feature description"`.
4. Push to your branch: `git push origin feature-name`.
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

- **Author:** [Your Name](https://github.com/yourusername)
- **Email:** your.email@example.com

---

Explore the projects and enhance your understanding of secure backend development!

