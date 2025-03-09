#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
It takes 3 arguments: MySQL username, password, and database name.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to fetch all states, ordered by id
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

    # Fetch all the results
    states = cursor.fetchall()

    # Display the results as required
    for state in states:
        print(state)

    # Close the cursor and the connection
    cursor.close()
    db.close()
