import logging

from lib.web import app

logger = logging.getLogger("http")


@app.route("/", methods=["GET"])
def index():
    logger.info("Hello, World!")
    return "Hello, World!"
