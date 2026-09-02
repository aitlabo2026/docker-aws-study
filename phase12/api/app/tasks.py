import os
from celery import Celery

celery_app = Celery("phase10", broker=os.environ["CELERY_BROKER_URL"], backend=os.environ["CELERY_RESULT_BACKEND"])
celery_app.conf.task_default_queue = "phase10-jobs"
celery_app.conf.broker_transport_options = {"region": os.environ["AWS_REGION"], "predefined_queues": {"phase10-jobs": {"url": os.environ["SQS_QUEUE_URL"]}}}

@celery_app.task(name="app.tasks.learning_job")
def learning_job(message: str = "completed"):
    return {"status":"completed","message":message}