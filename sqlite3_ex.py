

import sqlite3

# Connect 
conn = sqlite3.connect("example.db")
cur = conn.cursor()

# Create the table 
cur.execute("CREATE TABLE IF NOT EXISTS people (id INTEGER PRIMARY KEY, name TEXT)")

# Insert 
cur.execute("INSERT INTO people (name) VALUES (?)", ("Alice",))
conn.commit()

# Get and print all rows from the people table
for row in cur.execute("SELECT * FROM people"):
    print(row)

# Close the connection
conn.close()
