from .config import Config
from .controller.worker_controller import worker


def run():
    Config()
    worker()
