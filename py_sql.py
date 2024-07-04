import subprocess
import sys

# Function to install a package using pip
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Check if mysql-connector-python is installed, if not, install it
try:
    import mysql.connector
except ImportError:
    print("mysql-connector-python not found, installing...")
    install_package("mysql-connector-python")
    import mysql.connector

from mysql.connector import Error

def connect_to_db(host, user, password, database):
    """ Connect to a MySQL database and return the connection object """
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if conn.is_connected():
            print(f"Connected to database {database}")
            return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

def list_tables(conn):
    """ List all tables in the database """
    try:
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        print("Tables in the database:")
        for table in tables:
            print(table[0])
    except Error as e:
        print(f"Error listing tables: {e}")

def view_table_contents(conn, table_name):
    """ View the contents of a specific table """
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        col_names = [i[0] for i in cursor.description]
        print(f"Contents of table {table_name}:")
        print(col_names)
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error viewing table contents: {e}")

def check_table_content(conn, table_name, condition):
    """ Check if the table contains specific content based on the condition """
    try:
        cursor = conn.cursor()
        query = f"SELECT * FROM {table_name} WHERE {condition}"
        cursor.execute(query)
        rows = cursor.fetchall()
        if rows:
            print(f"The table {table_name} contains the content based on the condition '{condition}':")
            for row in rows:
                print(row)
        else:
            print(f"The table {table_name} does not contain any content based on the condition '{condition}'.")
    except Error as e:
        print(f"Error checking table content: {e}")

def main():
    host = input("Enter the host: ")
    user = input("Enter the username: ")
    password = input("Enter the password: ")
    database = input("Enter the name of the database: ")
    
    conn = connect_to_db(host, user, password, database)
    if conn:
        list_tables(conn)
        action = input("Do you want to view table contents or check specific content? (view/check/exit): ")
        while action.lower() != 'exit':
            if action.lower() == 'view':
                table_name = input("Enter the name of the table to view its contents: ")
                view_table_contents(conn, table_name)
            elif action.lower() == 'check':
                table_name = input("Enter the name of the table to check its contents: ")
                condition = input("Enter the condition to check (e.g., column_name = 'value'): ")
                check_table_content(conn, table_name, condition)
            else:
                print("Invalid option. Please enter 'view' or 'check'.")
            action = input("Do you want to view table contents or check specific content? (view/check/exit): ")
        conn.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
