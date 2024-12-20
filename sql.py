import mysql.connector
from mysql.connector import Error


#Connection to mysql server
def connect_to_mysql():
    connection = None  # Initialize connection variable
    try:
        # Establish connection
        connection = mysql.connector.connect(
            host='localhost',      # Replace with your hostname
            user='root',           # Replace with your MySQL username
            password='root',# Replace with your MySQL password
            database='colonial' # Replace with your database name

        )
#check if the connection is successful
        if connection.is_connected():
            print("Connected to MySQL Workbench!")
            
            # Create a cursor to execute SQL queries
            cursor = connection.cursor()
            
            # Example query: Show tables
            cursor.execute("SHOW TABLES;")
            tables = cursor.fetchall()
            print("Tables in the database:")
            for table in tables:
                print(table)
            
            # Close the cursor
            cursor.close()
    #Error handling
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if connection and connection.is_connected():  # Ensure connection exists before closing
            connection.close()
            print("MySQL connection closed.")

# Call the function
connect_to_mysql()
