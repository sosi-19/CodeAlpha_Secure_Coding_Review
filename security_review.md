# Secure Coding Review

## 1. Project Overview

This project demonstrates common security vulnerabilities in Python applications and how to fix them using secure coding practices.

The application uses Python and SQLite to demonstrate secure user registration, password hashing, authentication, and input validation.

## 2. Identified Security Vulnerabilities

| Vulnerability | Risk | Security Improvement |
|---|---|---|
| Hardcoded credentials | Attackers may discover sensitive credentials. | Avoid storing credentials directly in source code. |
| MD5 password hashing | MD5 is not suitable for password storage. | Use PBKDF2-HMAC-SHA256 with a random salt. |
| SQL injection | Attackers may manipulate database queries. | Use parameterized SQL queries. |
| Missing input validation | Invalid or unexpected data may enter the application. | Validate user input before processing. |
| Weak password storage | Exposed passwords could compromise user accounts. | Store salted password hashes instead of plaintext passwords. |

## 3. Security Improvements Implemented

### Password Hashing
Used PBKDF2-HMAC-SHA256 with 600,000 iterations and a random 16-byte salt.

### SQL Injection Prevention
Used parameterized SQL queries instead of joining user input directly into SQL statements.

### Password Verification
Used `hmac.compare_digest()` to compare password hashes safely.

### Input Validation
Added age validation to accept only numeric ages between 1 and 120.

### User Registration
Added checks for empty usernames, empty passwords, and duplicate usernames.

## 4. Security Testing Results

| Test Case | Expected Result | Actual Result |
|---|---|---|
| Valid registration | Registration successful | Passed |
| Correct password | Login successful | Passed |
| Incorrect password | Login rejected | Passed |
| SQL injection attempt | Login rejected | Passed |
| Invalid age (150) | Age rejected | Passed |

## 5. Technologies Used

- Python
- SQLite
- hashlib
- secrets
- hmac
- getpass

## 6. Conclusion

This project demonstrates how common security vulnerabilities can be identified and addressed through secure coding practices.

The improved application uses secure password hashing, parameterized SQL queries, password verification, and input validation.

The project is a learning prototype and should receive additional security testing before production use.