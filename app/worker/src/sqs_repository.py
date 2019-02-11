# coding=utf-8
import boto3
import os
import etcd


class WorkerSQSRepository:

    def __init__(self):
        self.client = etcd.Client(host=os.environ.get('SERVICE_DISCOVERY'), port=2379)
        self.sqs = boto3.resource(
            'sqs',
            aws_access_key_id=self.client.read('aws_access_key_id').value,
            aws_secret_access_key=self.client.read('aws_secret_access_key').value,
            region_name='us-east-1'
        )

        self.queue = self.sqs.get_queue_by_name(QueueName=self.client.read('sqs_name').value)

    def get_messages(self):
        messages = self.queue.receive_messages(
            WaitTimeSeconds=5,
            MaxNumberOfMessages=10,
            MessageAttributeNames=['All']
        )
        return messages

    def delete_message(self, messages_to_delete):
        self.queue.delete_messages(Entries=messages_to_delete)