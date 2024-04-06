import sqlite3

 

class AdvancedUserOperations:

    def __init__(self):

        self.conn = sqlite3.connect('advancedatabase.sqlite')

        self.cursor = self.conn.cursor()

 

    def create_user_with_profile(self, name, email, password, age=None, gender=None, address=None):
        self.conn = sqlite3.connect('advancedatabase.sqlite')
        cursor = self.conn.cursor()
        query = "INSERT INTO advancedatabase (name, email, password, age, gender, address) VALUES (?, ?, ?, ?, ?, ?)"
        values = (name, email, password, age, gender, address)

        cursor.execute(query, values)
        self.conn.commit()
        self.conn.close()
        

 

    def retrieve_users_by_criteria(self, min_age=None, max_age=None, gender=None):
        conn = sqlite3.connect('advancedatabase.sqlite')
        cursor = conn.cursor()

    # Write the SQL query to select users within the specified age range
        query = "SELECT * FROM advancedatabase WHERE age BETWEEN ? AND ?"
        cursor.execute(query, (min_age, max_age))

    # Fetch the results
        users = cursor.fetchall()

    # Close the database connection
        conn.close()

    # Return the fetched users
        return users
        

 

    def update_user_profile(self, email, age=None, gender=None, address=None):

        self.conn = sqlite3.connect('mydatabase.sqlite')
        cursor = self.conn.cursor()

        query = "UPDATE users SET"
        updates = []

        
        if email is not None:
            updates.append(f" email = '{email}'")
        if age is not None:
            updates.append(f" age = {age}")
        if gender is not None:
            updates.append(f" gender = '{gender}'")
        if address is not None:
            updates.append(f" address = '{address}'")

        # Join the updates into a single string
        query += ", ".join(updates)

        # Add the condition to update a specific user
        query += f" WHERE id = {self}"

        # Execute the query
        cursor.execute(query)

        # Commit the transaction
        self.conn.commit()

        # Close the database connection
        self.conn.close()

 

    def delete_users_by_criteria(self, gender=None):

        self.conn = sqlite3.connect('mydatabase.sqlite')
        cursor = self.conn.cursor()

        # Prepare the SQL query to delete users based on the specified criteria
        query = "DELETE FROM users WHERE"

        # Construct the WHERE clause based on the provided criteria
        conditions = []
        for key, value in gender.items():
            conditions.append(f" {key} = '{value}'")
        where_clause = " AND".join(conditions)

        # Append the WHERE clause to the query
        query += where_clause

        # Execute the query
        cursor.execute(query)

        # Commit the transaction
        self.conn.commit()

        # Close the database connection
        self.conn.close()

 

    def __del__(self):

        self.conn.close()

 