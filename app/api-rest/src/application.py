#!/usr/bin/python
from flask import Flask

from sugestao_resource import SugestaoResource


app = Flask(__name__)
SugestaoResource(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0')