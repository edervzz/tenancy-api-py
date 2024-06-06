"""_summary_"""

from toolkit.logger import LoggerAbstract

PREFIX_VER_1 = "/tenants/api/v1"


class Services:
    """_summary_
    """

    def __init__(self, mysql, logger: LoggerAbstract):
        self.mysql = None
        self.mysql = mysql
        self.logger = logger
