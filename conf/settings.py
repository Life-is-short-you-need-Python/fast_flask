import os

import environs
from environs import Env

env = Env()

environs.Env.read_env(os.path.join(str(environs.Path(__file__) - 1), "local.env"))

# log config
LOG_CONFIG_PATH = env.str("LOG_CONFIG_PATH")
LOG_PATH = env.str("LOG_PATH")

# server config
SERVER_HOST = env.str("SERVER_HOST")
SERVER_PORT = env.str("SERVER_PORT")
DEBUG = env.bool("DEBUG")
