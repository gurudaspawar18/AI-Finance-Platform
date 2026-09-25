import sqlite3
from werkzeug.security import generate_password_hash


# Connect to database
connection = sqlite3.connect("finance.db")
cursor = connection.cursor()


print("Password update started.")


# -----------------------------------------
# User 1
# -----------------------------------------

username1 = "user1"
password1 = "1234"

hashed_password1 = generate_password_hash(password1)

cursor.execute(
    """
    UPDATE users
    SET password = ?
    WHERE username = ?
    """,
    (hashed_password1, username1)
)


# -----------------------------------------
# User 2
# -----------------------------------------

username2 = "user2"
password2 = "1234"

hashed_password2 = generate_password_hash(password2)

cursor.execute(
    """
    UPDATE users
    SET password = ?
    WHERE username = ?
    """,
    (hashed_password2, username2)
)


# Save changes
connection.commit()

connection.close()


print("Passwords updated successfully!")
print("User 1 password: 1234")
print("User 2 password: 1234")