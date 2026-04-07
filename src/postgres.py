import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_connection():
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT", "5432")
    )
    return connection

if __name__ == "__main__":
    try:
        conn = get_connection()
        print("Connected to the database")
        cursor = conn.cursor()
        create_table_query = """ CREATE TABLE IF NOT EXISTS ridership (
                Unnamed_0 INT,
                transit_timestamp TIMESTAMP,
                station_complex_id VARCHAR(50),
                station_complex VARCHAR(200),
                borough VARCHAR(100),
                payment_method VARCHAR(50),
                ridership INT,
                transfers INT,
                latitude FLOAT,
                longitude FLOAT,
                Georeference VARCHAR(255)
            );
            """
        cursor.execute(create_table_query)
        conn.commit()
        print("Table Ridership created successfully !")
        cursor.close()
        conn.close()
    except Exception as e:
        print("Connection failed:", e)
