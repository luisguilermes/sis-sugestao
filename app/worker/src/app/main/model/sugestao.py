from mongoengine import Document, StringField


class Sugestao(Document):
    nome = StringField(required=True)
    email = StringField(max_length=100)
    sugestao = StringField(max_length=255)

    def __str__(self):
        return "=== Nome: {0} \n=== Email: {1} \n=== Sugestao: {2}".format(self.nome, self.email, self.sugestao)