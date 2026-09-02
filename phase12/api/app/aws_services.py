import os
import boto3
import psycopg
import redis
from fastapi import APIRouter, Body
from fastapi.responses import Response

router = APIRouter(prefix="/api/aws", tags=["aws"])

@router.get("/health")
def aws_health():
    with psycopg.connect(host=os.environ["POSTGRES_HOST"], dbname=os.environ["POSTGRES_DB"], user=os.environ["POSTGRES_USER"], password=os.environ["POSTGRES_PASSWORD"]) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            database = cursor.fetchone()[0] == 1
    cache = redis.Redis(host=os.environ["REDIS_HOST"], port=int(os.environ.get("REDIS_PORT", "6379"))).ping()
    region = os.environ["AWS_REGION"]
    sqs = boto3.client("sqs", region_name=region)
    sqs.get_queue_attributes(QueueUrl=os.environ["SQS_QUEUE_URL"], AttributeNames=["QueueArn"])
    s3 = boto3.client("s3", region_name=region)
    s3.head_bucket(Bucket=os.environ["S3_BUCKET"])
    return {"api":"ok","database":database,"redis":cache,"sqs":True,"s3":True}

@router.put("/files/{name}")
def put_file(name: str, body: bytes = Body()):
    boto3.client("s3", region_name=os.environ["AWS_REGION"]).put_object(Bucket=os.environ["S3_BUCKET"], Key=name, Body=body)
    return {"name":name,"stored":True}

@router.get("/files/{name}")
def get_file(name: str):
    item=boto3.client("s3", region_name=os.environ["AWS_REGION"]).get_object(Bucket=os.environ["S3_BUCKET"], Key=name)
    return Response(content=item["Body"].read(), media_type=item.get("ContentType", "application/octet-stream"))