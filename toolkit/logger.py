"""_summary_
    """
from abc import ABC, abstractmethod
import logging


class LoggerAbstract(ABC):
    """_summary_
    """

    def __init__(self):
        pass

    @abstractmethod
    def info(self, text: str):
        """_summary_"""


class LoggerBasic(LoggerAbstract):
    """_summary_"""

    def __init__(self):
        logging.basicConfig(
            format='%(levelname)s:%(message)s', level=logging.DEBUG)

    def info(self, text: str):
        print("error")
        logging.info(text)
        print("error")
