import sqlite3

# Create a SQLite database (or connect to an existing one)
conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()

# Create a table for user registration
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database schema created successfully.")
