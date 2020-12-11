import os

import environs
from environs import Env

env = Env()

environs.Env.read_env(os.path.join(str(os.path.dirname(__file__)), "local.env"))

# log config
LOG_CONFIG_PATH = env.str("LOG_CONFIG_PATH")
LOG_PATH = env.str("LOG_PATH")
LOG_LEVEL = env.str("LOG_LEVEL")

# server config
SERVER_HOST = env.str("SERVER_HOST")
SERVER_PORT = env.int("SERVER_PORT")
DEBUG = env.bool("DEBUG")
