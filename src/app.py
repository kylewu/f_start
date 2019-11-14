
from flask import Flask
# from flask_cors import CORS

from db import db
from apis import api
import settings

def create_default_admin(app):
    with app.app_context():
        from db.models import User
        if not User.objects(handle='admin'):
            app.logger.warning('Creating default user')
            User(**{'handle': 'admin'}).save()


def create_app():
    """
    Create flask app
    """
    app = Flask(__name__)
    # CORS(app)

    app.config['MONGODB_SETTINGS'] = {
        'db': settings.MONGODB_SETTINGS_DB,
        'username': settings.MONGODB_SETTINGS_USERNAME,
        'password': settings.MONGODB_SETTINGS_PASSWORD,
        'host': settings.MONGODB_SETTINGS_HOST,
        'port': settings.MONGODB_SETTINGS_PORT
    }

    app.config['PORT'] = settings.PORT
    # app.config['ERROR_404_HELP'] = False
    app.config['DEBUG'] = True
    db.init_app(app)

    api.init_app(app)
    create_default_admin(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=app.config["PORT"])
