"""Create an application instance."""
from flask import jsonify
from flask.helpers import get_debug_flag

from app.services.format_response import formatSuccess, formatError
from app.app import create_app
from app.settings import DevConfig, ProdConfig

CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = create_app(CONFIG)

@app.route('/')
def init():
    return formatSuccess()