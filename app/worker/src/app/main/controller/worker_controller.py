from ..repository.sqs_repository import sqs_get_messages, sqs_delete_messages
from ..model.sugestao import Sugestao

import os
from mongoengine import *


def get_mongo_connection():
    return connect('sugestao_db', host=os.environ.get('DB_NAME'))


def worker():
    get_mongo_connection()
    while True:

        messages = sqs_get_messages()
        for message in messages:

            nova_sugestao = Sugestao(
                nome=message['MessageAttributes']['Nome']['StringValue'],
                email=message['MessageAttributes']['Email']['StringValue'],
                sugestao=message['Body']
            )
            nova_sugestao.save()

        if messages:
            messages_to_delete = [
                {'Id': msg['MessageId'], 'ReceiptHandle': msg['ReceiptHandle']}
                for msg in messages
            ]
            print(messages_to_delete)
            sqs_delete_messages(messages_to_delete)