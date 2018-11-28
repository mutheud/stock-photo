from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)

    # Initializing flask extensions
    bootstrap.init_app(app)
    
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    
    return app
