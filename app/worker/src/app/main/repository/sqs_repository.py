import boto3

from app.main.config import Config as config


def sqs_get_messages():
    client = boto3.client(
        'sqs',
        aws_access_key_id=config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
        region_name='us-east-1'
    )
    resp = client.receive_message(
        QueueUrl=config.SQS_ID,
        WaitTimeSeconds=2,
        MaxNumberOfMessages=10,
        MessageAttributeNames=['All']
    )
    try:
        messages = resp['Messages']
    except KeyError:
        messages = []
        print("Queue está limpa!")
    return messages


def sqs_delete_messages(messages_to_delete):
    client = boto3.client(
        'sqs',
        aws_access_key_id=config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
        region_name='us-east-1'
    )
    client.delete_message_batch(
        QueueUrl=config.SQS_ID, Entries=messages_to_delete
    )
