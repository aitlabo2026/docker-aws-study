import os
import psycopg
import redis
from celery.result import AsyncResult
from fastapi import Depends, FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from .auth import current_user
from .tasks import celery_app, learning_job

app = FastAPI(title="Phase 3 API")
Instrumentator().instrument(app).expose(app)

def db_connection():
    return psycopg.connect(host="db", dbname=os.environ["POSTGRES_DB"], user=os.environ["POSTGRES_USER"], password=os.environ["POSTGRES_PASSWORD"])

@app.get("/api/health")
def health():
    with db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            database = cursor.fetchone()[0] == 1
    cache = redis.Redis(host="redis", port=6379).ping()
    return {"api": "ok", "database": database, "redis": cache}

@app.get("/api/secure")
def secure(user=Depends(current_user)):
    return {"message": f"authenticated as {user['username']}", "roles": user["roles"]}

@app.post("/api/jobs")
def create_job(user=Depends(current_user)):
    task = learning_job.delay(user["username"])
    return {"task_id": task.id, "state": task.state}

@app.get("/api/jobs/{task_id}")
def job_status(task_id: str, user=Depends(current_user)):
    task = AsyncResult(task_id, app=celery_app)
    return {"task_id": task_id, "state": task.state, "result": task.result if task.successful() else None}
