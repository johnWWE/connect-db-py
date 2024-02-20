import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

try:
    # Get the values ​​of environment variables
    dbname = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")

    # Connect to database using environment variables
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print("Successful connection")
    conn.close()
except Exception as e:
    print("Connection error:", e)
