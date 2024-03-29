import sqlite3

# Connect to the SQLite database
connectTo = sqlite3.connect('') # jas' database

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table (if it doesn't exist)
cursor.execute('''CREATE table if it doesn't exist alr''')

# Insert our data from published messages into the table
cursor.execute("INSERT INTO users (BikeID, longitude, latitude) VALUES ('', '')", ('', ''))
cursor.execute("INSERT INTO users (BikeID, longitude, latitude) VALUES ('', '')", ('', ''))

# Commit the changes
connectTo.commit()

# Execute a SELECT query
cursor.execute("SELECT * FROM '#DB name'")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
connectTo.close()