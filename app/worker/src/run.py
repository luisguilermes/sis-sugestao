# coding=utf-8
import os
from mongoengine import *

from sqs_repository import WorkerSQSRepository


class Sugestao(Document):
    nome = StringField(required=True)
    email = StringField(max_length=100)
    sugestao = StringField(max_length=255)


def worker():
    connect('sugestao_db', host=os.environ.get('DB_NAME'))
    sqs = WorkerSQSRepository()
    while 1:
        messages_to_delete = []

        for message in sqs.get_messages():
            nova_sugestao = Sugestao(
                nome=message.message_attributes['Nome']['StringValue'],
                email=message.message_attributes['Email']['StringValue'],
                sugestao=message.body
            )
            nova_sugestao.save()
            messages_to_delete.append({
                'Id': message.message_id,
                'ReceiptHandle': message.receipt_handle
            })

        if len(messages_to_delete) == 0:
            pass
        else:
            sqs.delete_message(messages_to_delete)

        print("[INFO] - Sugestoes inseridas no Mongo")
        cont = 0
        for sugestao in Sugestao.objects:
            print(sugestao.email)
            cont+=1
        print("================ {} ".format(cont))


if __name__ == '__main__':
    worker()