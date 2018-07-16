from flask import Blueprint
from flask_restplus import Api


app = Blueprint('app', __name__)

api = Api(
    app,
    version='1.0',
    title='Y2K API',
    # description='Y2K API',
    default='Endpoints',
    default_label='Y2K API Resources',
    )

from . import routes