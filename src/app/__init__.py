import logging
from flask import Flask


def create_app(config):

    logging.info('STARTUP: Launching a Flask App')

    app = Flask(__name__)
    app.config.update(config)

    # Frontend blueprint
    from .main import app as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    # API blueprint
    from .api import app as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    logging.info('STARTUP: READY TO ROCK!!!')

    return app



