# CodeAlpha Secure Coding Review

## Project Overview

This project demonstrates common security vulnerabilities in Python applications and how to prevent them using secure coding practices.

It compares vulnerable coding techniques with improved security implementations.

## Project Objectives

- Identify common security vulnerabilities.
- Understand SQL injection attacks.
- Implement secure password hashing.
- Prevent unauthorized access.
- Validate user input.
- Apply secure database operations.

## Technologies Used

- Python
- SQLite
- hashlib
- secrets
- hmac
- getpass

## Project Structure

```text
CodeAlpha_Secure_Coding_Review/
│
├── vulnerable_app.py
├── secure_app.py
├── security_review.md
├── requirements.txt
└── README.md
```

## Security Features

### 1. Password Hashing
Uses PBKDF2-HMAC-SHA256 with a random salt to protect stored passwords.

### 2. SQL Injection Prevention
Uses parameterized SQL queries to prevent SQL injection attacks.

### 3. Secure Password Verification
Uses `hmac.compare_digest()` to compare password hashes.

### 4. Input Validation
Validates age input and accepts values between 1 and 120.

### 5. Duplicate Username Prevention
Prevents users from registering with an existing username.

## How to Run

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the project folder

```bash
cd CodeAlpha_Secure_Coding_Review
```

### Step 3: Run the secure application

```bash
python secure_app.py
```

## Testing

The following security tests were performed:

- Successful user registration.
- Successful login with the correct password.
- Rejection of incorrect passwords.
- SQL injection attempt rejection.
- Invalid age rejection.

## Conclusion

This project demonstrates practical secure coding techniques and highlights the importance of protecting user information, preventing database attacks, and validating input.