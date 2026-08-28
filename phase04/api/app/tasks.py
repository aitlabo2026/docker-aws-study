from datetime import datetime, timezone
from celery import Celery

celery_app = Celery(
    "phase03",
    broker="redis:" + "//redis:6379/0",
    backend="redis:" + "//redis:6379/1",
)
celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True,
)

@celery_app.task(name="phase03.learning_job")
def learning_job(username):
    return {"status": "completed", "username": username, "completed_at": datetime.now(timezone.utc).isoformat()}