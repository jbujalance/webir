from flask import Flask


def create_app():
    """
    Flask application factory.
    :return: The instance of the Flask application.
    """
    app = Flask(__name__)
    app.config.from_object('webir.config')
    # TODO maybe use the instance configurations instead of the setting the path in the env: https://flask.palletsprojects.com/en/master/config/#instance-folders
    app.config.from_envvar('WEBIR_CONFIGURATION', silent=True)

    from .converters import ListConverter
    app.url_map.converters[ListConverter.NAME] = ListConverter

    with app.app_context():
        from . import routes
        app.register_blueprint(routes.remote_blueprint)

    return app
