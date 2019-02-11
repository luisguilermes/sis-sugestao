
from app.main.model.sugestao import Sugestao
from app.main.repository.sqs_repository import sqs_add


def create_sugestao(data):
    new_sugestao = Sugestao(
        data['nome'],
        data['email'],
        data['sugestao']
    )
    response_object = save_sqs(new_sugestao)
    # response_object = {
    #     'status': 'success',
    #     'message': 'Successfully registered.'
    # }
    return response_object


def save_sqs(data):
    return sqs_add(data=data)

