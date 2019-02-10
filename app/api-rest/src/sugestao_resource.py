# -*- coding: utf-8 -*-
import json

from flask import request, jsonify, make_response
import socket

from sugestao_service import SugestaoService
from sugestao import Sugestao


class SugestaoResource():

    def __init__(self, app):
        @app.route("/info", methods = ['GET'])
        def home_index():
            api_list = [
                {
                    'version'   : 'v1',
                    'buildtime' : '2019-02-08',
                    'links'     : '/sugestao',
                    'methods'   : 'get, post',
                    'host'      : socket.gethostname()
                }
            ]
            return jsonify({'api_version': api_list}), 200

        @app.route('/sugestao', methods=['POST'])
        def create_sugestao():
            json_data = json.loads(request.data)
            print("=============> JSON_DATA: {}".format(json_data))
            nova_sugestao = Sugestao(
                json_data['nome'],
                json_data['email'],
                json_data['sugestao'])
            result = SugestaoService().add_sugestao(nova_sugestao)
            return jsonify({'status': result}), 201


        @app.errorhandler(404)
        def resource_not_found(error):
            return make_response(jsonify({'error': 'Resource not found!'}), 404)


        @app.errorhandler(409)
        def user_found(error):
            return make_response(jsonify({'error': 'Conflict! Record exist'}), 409)


        @app.errorhandler(400)
        def invalid_request(error):
            return make_response(jsonify({'error': 'Bad Request'}), 400)
