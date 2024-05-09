import sqlite3

# Connect to the database
conn = sqlite3.connect('coffeeteria.db')
cursor = conn.cursor()

# Execute a query to fetch all records from the users table
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

# Display the retrieved data
for row in rows:
    print(row)

# Close the connection
conn.close()
