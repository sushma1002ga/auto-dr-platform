from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

DB_HOST = os.getenv("DB_HOST", "db")

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database="demo",
        user="postgres",
        password="postgres"
    )

@app.get("/")
def root():
    return {"status": "running"}

@app.get("/users")
def users():

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("SELECT * FROM users")

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return {"users": rows}
