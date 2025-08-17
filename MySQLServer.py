import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Password2025#!'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            try:
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except Error as e:
                print(f"Error creating database: {e}")
            finally:
                cursor.close()
                connection.close()
                print("Connection closed.")
    except Error as e:
        print(f"Error connecting to MySQL: {e}")

if __name__ == "__main__":
    create_database()
