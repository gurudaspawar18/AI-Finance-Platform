import sqlite3

print("Starting database update...")

# Connect to database
connection = sqlite3.connect("finance.db")
cursor = connection.cursor()

try:

    cursor.execute("""
        ALTER TABLE expenses
        ADD COLUMN user_id INTEGER
    """)

    print("user_id column added successfully!")

except sqlite3.OperationalError as error:

    print("Database message:", error)

connection.commit()
connection.close()

print("Database update completed successfully!")