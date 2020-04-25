from flask import Flask


def create_app(config_filename='../config.py'):
    """
    Flask application factory.
    :param config_filename: The name of the configuration file to load.
    :return: The instance of the Flask application.
    """
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    from .converters import ListConverter
    app.url_map.converters[ListConverter.NAME] = ListConverter

    with app.app_context():
        from . import routes
        app.register_blueprint(routes.remote_blueprint)

    return app
