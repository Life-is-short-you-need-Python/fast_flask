from common.web import app
from conf import settings

if __name__ == "__main__":
    app.run(host=settings.SERVER_HOST, port=settings.SERVER_PORT, debug=True)
