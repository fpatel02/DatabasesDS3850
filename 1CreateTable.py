import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('DatabaseFile.db')

# Create a cursor object
cursor = conn.cursor()

# Create the StudentInfo table
cursor.execute('''
CREATE TABLE IF NOT EXISTS StudentInfo (
    StudentID INTEGER PRIMARY KEY,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully in DatabaseFile.db.")
