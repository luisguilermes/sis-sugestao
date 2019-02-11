import os
import sys
import etcd
import logging
import time



class Config:
    """ Class Config - Classe responsável por validar e configurar aplicação"""
    logging.basicConfig(level=logging.ERROR, format=' %(levelname)s - %(asctime)s - %(message)s')

    SERVICE_DISCOVERY = os.environ.get('SERVICE_DISCOVERY')
    if SERVICE_DISCOVERY is None:
        logging.error("Variavel de ambiente SERVICE_DISCOVERY não foi definida.")
        sys.exit(4)

    try:
        AWS_ACCESS_KEY_ID = etcd.Client(
            host=os.environ.get('SERVICE_DISCOVERY'),
            port=2379).read('aws_access_key_id').value
    except Exception as err:
        logging.error("{}".format(err))
        time.sleep(10)
        sys.exit(4)

    try:
        AWS_SECRET_ACCESS_KEY = etcd.Client(
            host=os.environ.get('SERVICE_DISCOVERY'),
            port=2379).read('aws_secret_access_key').value
    except Exception as err:
        logging.error("{}".format(err))
        time.sleep(10)
        sys.exit(4)

    try:
        SQS_ID = etcd.Client(
            host=os.environ.get('SERVICE_DISCOVERY'),
            port=2379).read('sqs_id').value
    except Exception as err:
        logging.error("{}".format(err))
        time.sleep(10)
        sys.exit(4)


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    prod=ProductionConfig
)
