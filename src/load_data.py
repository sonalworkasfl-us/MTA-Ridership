import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connect to RDS
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT")
)
cursor = conn.cursor()

# Run COPY FROM S3
copy_sql = f"""
COPY ridership
FROM 's3://my-ridership/ridership_clean.csv'
IAM_ROLE 'arn:aws:iam::255399219140:role/RDS-S3-ReadRole'
CSV HEADER;
"""

cursor.execute(copy_sql)
conn.commit()

print("✅ Successfully imported data from S3 into RDS.")

cursor.close()
conn.close()
