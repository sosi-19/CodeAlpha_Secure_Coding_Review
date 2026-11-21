import sqlite3
import hashlib
import secrets
import hmac
import getpass


DATABASE = "secure_users.db"


# Connect to database and create users table
def initialize_database():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            salt TEXT NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


# Secure password hashing using PBKDF2
def hash_password(password, salt=None):

    if salt is None:
        salt = secrets.token_bytes(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        600000
    )

    return salt.hex(), password_hash.hex()


# Register a new user
def register_user(username, password):

    if not username or not password:
        print("Username and password cannot be empty.")
        return False

    salt, password_hash = hash_password(password)

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO users (username, salt, password_hash)
            VALUES (?, ?, ?)
            """,
            (username, salt, password_hash)
        )

        connection.commit()
        print("User registered successfully!")
        return True

    except sqlite3.IntegrityError:
        print("Username already exists.")
        return False

    finally:
        connection.close()


# Secure login
def login_user(username, password):

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT salt, password_hash FROM users WHERE username = ?",
        (username,)
    )

    user = cursor.fetchone()
    connection.close()

    if user is None:
        print("Invalid username or password.")
        return

    salt = bytes.fromhex(user[0])

    _, entered_hash = hash_password(password, salt)

    if hmac.compare_digest(entered_hash, user[1]):
        print("Login successful!")
    else:
        print("Invalid username or password.")


# Validate age input
def validate_age(age):

    try:
        age = int(age)

        if age < 1 or age > 120:
            print("Invalid age. Enter an age between 1 and 120.")
            return False

        print("Valid age:", age)
        return True

    except ValueError:
        print("Age must be a number.")
        return False


# Main program
# Main program
if __name__ == "__main__":

    initialize_database()

    print("\n================================")
    print("       SECURE CODING REVIEW")
    print("================================")

    print("\n1. Register")
    print("2. Login")

    choice = input("\nChoose an option: ")

    if choice == "1":

        username = input("Enter username: ").strip()
        password = input("Enter password: ")

        print("\n--- User Registration ---")
        register_user(username, password)

    elif choice == "2":

        username = input("Enter username: ").strip()
        password = input("Enter password: ")

        print("\n--- User Login ---")
        login_user(username, password)

    else:
        print("Invalid choice.")

    print("\n--- Age Validation ---")
    age = input("Enter your age: ")
    validate_age(age)