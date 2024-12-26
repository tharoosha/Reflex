import pymysql
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database configuration from environment variables
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USERNAME = os.getenv("MYSQL_USERNAME")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))  # Default MySQL port is 3306
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "defaultdb")

# Timeout for the database connection
TIMEOUT = 10

def get_connection():
    """
    Creates and returns a new MySQL connection with error handling.
    """
    try:
        connection = pymysql.connect(
            host=MYSQL_HOST,
            user=MYSQL_USERNAME,
            password=MYSQL_PASSWORD,
            db=MYSQL_DATABASE,
            port=MYSQL_PORT,
            charset="utf8mb4",
            connect_timeout=TIMEOUT,
            read_timeout=TIMEOUT,
            write_timeout=TIMEOUT,
            cursorclass=pymysql.cursors.DictCursor,
        )
        return connection
    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        raise
