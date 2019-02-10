# coding=utf-8

from sugestao_repository import SugestaoRepository


class SugestaoService(object):

    def add_sugestao(self, sugestao):
        response = SugestaoRepository().publicar(
                        sugestao.email,
                        sugestao.nome,
                        sugestao.sugestao
                    )
        return response
