from conf import settings
from lib.web import app

app.load_routers()

if __name__ == "__main__":
    app.run(host=settings.SERVER_HOST, port=settings.SERVER_PORT, debug=settings.DEBUG)
