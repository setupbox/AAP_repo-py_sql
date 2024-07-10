import mysql.connector

# Function to connect to MySQL database and fetch data
def connect_and_fetch(host, database, user, password):
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()

            # Execute a SELECT query
            query = "SELECT * FROM test_table"
            cursor.execute(query)

            # Fetch all rows from the result set
            records = cursor.fetchall()

            # Print each row
            print("Printing fetched data:")
            for row in records:
                print(row)

    except mysql.connector.Error as error:
        print("Failed to fetch data from MySQL table: {}".format(error))

    finally:
        # Closing database connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Example usage:
if __name__ == "__main__":
    # Database connection details
    host = "localhost"
    database = "your_database_name"
    user = "your_username"
    password = "your_password"

    # Call the function to connect and fetch data
    connect_and_fetch(host, database, user, password)
