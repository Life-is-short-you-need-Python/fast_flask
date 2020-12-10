import logging
from logging import config


class Log(object):
    @classmethod
    def set_up(cls, log_cnf, log_port=""):
        log_port = "_" + str(log_port) if log_port else ""
        config.fileConfig(log_cnf["config_file"], defaults={"log_port": log_port})
        Log.logger = logging.getLogger(log_cnf["default_logger"])

    @staticmethod
    def get_log(log_name=None):
        logger = (
            logging.getLogger(log_name) if log_name else logging.getLogger("simple")
        )
        return logger
