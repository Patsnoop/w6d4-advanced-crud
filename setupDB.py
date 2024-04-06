import sqlite3
# Connect to the database (creates the database file if it doesn't exist)
con = sqlite3.connect("advancedatabase.sqlite")
# Create a cursor object
cur = con.cursor()
# Execute a SQL command to create a table (optional)
cur.execute('''CREATE TABLE IF NOT EXISTS advancedatabase (
                user INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT UNIQUE,
                password TEXT,
                age INTEGER,
                gender TEXT,
                address TEXT
            )''')



# # Execute a SQL command to select data from the table
# cur.execute("SELECT * FROM bloggingDatabase")
print(cur.fetchall())  # Output: [(1, 'Movie A', 2020)]
# Commit changes (if necessary)
con.commit()
# Close the connection
con.close()