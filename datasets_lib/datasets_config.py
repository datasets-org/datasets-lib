from typing import Tuple

from confobj import Config
from confobj import ConfigBase


class DatasetsConfig(Config):
    def __init__(self, order=None):
        # type: (Tuple[ConfigBase]) -> None
        self.host = "localhost"
        self.port = 8000
        self.ssl = False
        super().__init__(order=order)
        self.configure()
