from fastapi import FastAPI
import mysql.connector
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('.env')
load_dotenv()
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.on_event("startup")
async def on_startup():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password=os.getenv('DB_PASSWORD'),
        database='musirate'
    )

    cursor = connection.cursor()
    print("Connected to database")
