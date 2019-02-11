import boto3

from app.main.config import Config as config


def sqs_client():
    return boto3.client(
        'sqs',
        aws_access_key_id=config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
        region_name='us-east-1'
    )