from flask_restplus import Namespace, fields


class SugestaoDto:
    api = Namespace('sugestao', description='operações relacionadas a sugestões')
    sugestao = api.model('sugestao', {
        'nome': fields.String(required=True, description='Nome da pessoa.'),
        'email': fields.String(required=True, description='Email da pessoa.'),
        'sugestao': fields.String(required=True, description='Mensagem de sugestão.')
    })
