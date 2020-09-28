from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
# from flask_uploads import UploadSet,configure_uploads,IMAGES


bootstrap = Bootstrap()
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

def create_app(config_name):

    app = Flask(__name__)
    app.debug = True

    # App Configurations
    app.config.from_object(config_options[config_name])

    # Initialize flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Register main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Register auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    # Register errors blueprint
    from .errors import errors as errors_blueprint
    app.register_blueprint(errors_blueprint)

    return app