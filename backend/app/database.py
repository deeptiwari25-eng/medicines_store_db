import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    # Use DATABASE_URL from environment variable
    db_url = os.environ.get('DATABASE_URL')
    
    if not db_url:
        raise ValueError("DATABASE_URL environment variable is missing from Vercel settings.")

    try:
        # Ensure SSL mode is enabled for Neon/Vercel if not already in URL
        if 'sslmode' not in db_url and 'localhost' not in db_url:
            db_url += '?sslmode=require'
            
        conn = psycopg2.connect(db_url)
        return conn
    except Exception as e:
        # Re-raise the exception so the calling function can display the exact error
        raise e
