import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Password2025#!'  
        )

        cursor = connection.cursor()

       
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except Error as err:
        print(f"Error: {err}")

    finally:
        
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print("Connection closed.")

if __name__ == "__main__":
    create_database()
