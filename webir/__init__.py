from flask import Flask
from flask_of_oil import OAuthFilter


def create_app():
    """
    Flask application factory.
    :return: The instance of the Flask application.
    """
    app = Flask(__name__)
    app.config.from_object('webir.config')
    # TODO maybe use the instance configurations instead of the setting the path in the env: https://flask.palletsprojects.com/en/master/config/#instance-folders
    app.config.from_envvar('WEBIR_CONFIGURATION', silent=True)

    # Register converters
    from .converters import ListConverter
    app.url_map.converters[ListConverter.NAME] = ListConverter

    # Register routes
    with app.app_context():
        from . import routes
        app.register_blueprint(routes.remote_blueprint)

    # Configure authentication
    oauth = OAuthFilter(verify_ssl=False)
    oauth.configure_with_jwt(
        jwks_url=app.config.get("AUTH_JWKS_URL"),
        issuer=app.config.get("AUTH_ISSUER"),
        audience=app.config.get("AUTH_AUDIENCE"),  # Only the access tokes issued to the Alexa skill are valid in the WebIR service
        scopes=[app.config.get("AUTH_SCOPE")]  # All the endpoints are protected with the same scope.
    )
    app.before_request(oauth.filter)  # We apply the authorization filter to every endpoint in the application

    return app
