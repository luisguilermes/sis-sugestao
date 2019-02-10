# -*- coding: utf-8 -*-
import boto3
import os
import etcd


class SugestaoRepository:

    def __init__(self, ):
        self.client = etcd.Client(host=os.environ.get('SERVICE_DISCOVERY'), port=2379)
        self.sqs = boto3.client(
            'sqs',
            aws_access_key_id=self.client.read('aws_access_key_id').value,
            aws_secret_access_key=self.client.read('aws_secret_access_key').value,
            region_name='us-east-1'
        )

    def publicar(self, email, nome, body):
        response = self.sqs.send_message(
            QueueUrl=self.client.read('sqs_id').value,
            DelaySeconds=10,
            MessageAttributes={
                'Nome': {
                    'DataType': 'String',
                    'StringValue': '{}'.format(nome)
                },
                'Email': {
                    'DataType': 'String',
                    'StringValue': '{}'.format(email)
                },

            },
            MessageBody='{}'.format(body)

        )
        return response
