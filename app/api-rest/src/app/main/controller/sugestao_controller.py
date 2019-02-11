from flask import request
from flask_restplus import Resource

from app.main.util.dto import SugestaoDto
from app.main.service.sugestao_service import create_sugestao

api = SugestaoDto.api
_sugestao = SugestaoDto.sugestao



@api.route('')
class SugestaoList(Resource):
    @api.response(201, 'Sugestao criada com sucesso.')
    @api.doc('Criar nova sugestão')
    @api.expect(_sugestao, validate=True)
    def post(self):
        """"Cria uma nova sugestão"""
        data = request.json
        print(data)
        return create_sugestao(data=data), 201


@api.route('/healthcheck')
class SugestaoHealthcheck(Resource):
    def get(self):
        """Cria um path Healthcheck"""
        response_object = {
            'status': 'success',
            'message': 'Its alived!.'
        }
        return response_object, 200
