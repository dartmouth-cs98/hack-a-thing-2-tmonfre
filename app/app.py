"""The app module, containing the app factory function."""
from flask import Flask

from app import commands, routers
from app.settings import ProdConfig


def create_app(config_object=ProdConfig):
    """An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.
    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config_object)
    register_commands(app)
    register_blueprints(app)
    return app


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(routers.elections.api.blueprint)
    app.register_blueprint(routers.crawler.api.blueprint)
    return None


def register_commands(app):
    """Register Click commands."""
    app.cli.add_command(commands.test)
    app.cli.add_command(commands.urls)
