from fastapi import FastAPI
import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

# create connection
conn = psycopg2.connect(
    dbname=os.getenv('DB_NAME'), 
    user=os.getenv('DB_USER'), 
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
)

@app.get("/")
def getAll():
    return {
        "msg": "hello world!"
    }

@app.get('/profiles')
async def getProfiles():
    df = pd.read_sql("select * from profiles;", conn)

    return {
        "data": df.to_dict(orient="records")
    }