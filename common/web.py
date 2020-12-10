import logging
import os
from importlib.machinery import SOURCE_SUFFIXES, SourceFileLoader
from importlib.util import module_from_spec, spec_from_loader
from logging import config

from flask import Flask

from conf import settings


class XFlask(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_app()

    def init_app(self):
        self.load_routers()
        self.init_log_conf()

    def process_response(self, response):
        return super(XFlask, self).process_response(response)

    @staticmethod
    def load_routers(routers_name: str = "routers") -> None:
        """
        Automatic loading all of the routers py.
        :param routers_name: routers package name
        """
        for root_path, _, files in os.walk(routers_name, topdown=False):
            for file_name in files:
                suffixes = os.path.splitext(file_name)[1]
                file_path = os.path.join(root_path, file_name)
                if suffixes not in SOURCE_SUFFIXES or not os.path.isfile(file_path):
                    continue
                no_suffixes_py_name = os.path.splitext(file_name)[0]
                source_file_loader = SourceFileLoader(
                    "_biz_" + no_suffixes_py_name, file_path
                )
                spec = spec_from_loader(source_file_loader.name, source_file_loader)
                module = module_from_spec(spec)
                source_file_loader.exec_module(module)

    @staticmethod
    def init_log_conf(log_conf_path: str = settings.LOG_CONFIG_PATH):
        log_port = int(os.environ.get("port", settings.SERVER_PORT))
        config.fileConfig(
            log_conf_path,
            defaults={
                "log_path": f"{settings.LOG_PATH}",
                "log_port": f"{str(log_port)}",
            },
        )


app = XFlask(__name__)
