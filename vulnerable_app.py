
import sqlite3
import hashlib

# Example 1: Hardcoded credentials
USERNAME = "admin"
PASSWORD = "admin123"


# Example 2: Insecure password storage
def register_user(username, password):
    hashed_password = hashlib.md5(
        password.encode()
    ).hexdigest()

    print("User registered:", username)
    print("Stored password hash:", hashed_password)


# Example 3: SQL Injection vulnerability
def login_user(username, password):

    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    # Create a test users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        )
    """)

    # Insert a dummy test account
    cursor.execute("""
        INSERT INTO users (username, password)
        VALUES (?, ?)
    """, (USERNAME, PASSWORD))

    connection.commit()

    # Intentionally vulnerable SQL query
    query = (
        "SELECT * FROM users WHERE username = '"
        + username
        + "' AND password = '"
        + password
        + "'"
    )

    cursor.execute(query)

    result = cursor.fetchone()

    if result:
        print("Login successful!")
    else:
        print("Invalid username or password.")

    connection.close()


# Example 4: No input validation
def process_age(age):

    print("Your age is:", age)


# Main program
# Main program
if __name__ == "__main__":

    print("SECURE CODING REVIEW")
    print("--------------------")

    print("\n--- Insecure Password Storage ---")
    register_user("sosina", "mypassword123")

    print("\n--- Missing Input Validation ---")
    process_age(-10)

    print("\n--- SQL Injection Test ---")

    username = input("Enter username: ")
    password = input("Enter password: ")

    login_user(username, password)