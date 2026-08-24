import os

import psycopg
import redis
from fastapi import FastAPI

app = FastAPI(title="Phase 2 API")


def db_connection():
    return psycopg.connect(
        host=os.environ["POSTGRES_HOST"],
        dbname=os.environ["POSTGRES_DB"],
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
    )


@app.get("/")
def root():
    return {"service": "phase02-api"}


@app.get("/api/health")
def health():
    with db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            database = cursor.fetchone()[0] == 1
    cache = redis.Redis(host=os.environ["REDIS_HOST"], port=6379).ping()
    return {"api": "ok", "database": database, "redis": cache}


@app.get("/api/items")
def items():
    with db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, message FROM learning_check ORDER BY id")
            rows = cursor.fetchall()
    return [{"id": row[0], "message": row[1]} for row in rows]
