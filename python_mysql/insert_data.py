import mysql.connector

# Function to connect to MySQL database and insert data
def connect_and_insert(host, database, user, password, data):
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

            # Create a table (if it doesn't exist)
            create_table_query = """
            CREATE TABLE IF NOT EXISTS test_table (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                age INT NOT NULL
            )
            """
            cursor.execute(create_table_query)
            print("Table created successfully")

            # Insert data into the table
            insert_query = """
            INSERT INTO test_table (name, age) VALUES (%s, %s)
            """
            cursor.executemany(insert_query, data)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into test_table")

    except mysql.connector.Error as error:
        print("Failed to insert record into test_table {}".format(error))

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

    # Data to insert (list of tuples)
    data_to_insert = [
        ('John Doe', 30),
        ('Jane Smith', 25),
        ('Michael Johnson', 35)
    ]

    # Call the function to connect and insert data
    connect_and_insert(host, database, user, password, data_to_insert)
