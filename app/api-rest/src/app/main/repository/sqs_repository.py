from .sqs_factory import sqs_client
from app.main.config import Config as config


def sqs_add(data):
    response = sqs_client().send_message(
        QueueUrl=config.SQS_ID,
        DelaySeconds=30,
        MessageAttributes={
            'Nome': {
                'DataType': 'String',
                'StringValue': '{}'.format(data.nome)
            },
            'Email': {
                'DataType': 'String',
                'StringValue': '{}'.format(data.email)
            },

        },
        MessageBody='{}'.format(data.sugestao)

    )
    return response