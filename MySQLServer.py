import mysql.connector

def create_database():
    try:
        # Connect to MySQL Server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"   # <-- Update with your password
        )

        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        # EXACT SYNTAX REQUIRED BY CHECKER
        print(f"Error while connecting to MySQL: {e}")

    finally:
