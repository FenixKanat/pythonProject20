import mysql.connector

class DatabaseConnection:
    """Object that handles all interactions with the database."""

    def __init__(self):

        try:
            self.connection = mysql.connector.connect(
                user='root',
                password='root',
                host='localhost',
                database='org'
            )
            

        except mysql.connector.Error as error:
            print(f"Could not connect to the database, {error.errno}")

