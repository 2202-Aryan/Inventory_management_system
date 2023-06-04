import sqlite3

# Connect to the database (this will create the file if it doesn't exist)
conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

# Create the Products table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        stock INTEGER NOT NULL
    )
''')

# Save the changes and close the connection
conn.commit()
conn.close()
