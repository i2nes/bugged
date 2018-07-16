from app import create_app
from app_config import flask_config


app = create_app(flask_config)