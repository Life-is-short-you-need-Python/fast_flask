from common.web import app


@app.route("/", methods=["GET"])
def index():
    return "Hello, World!"
