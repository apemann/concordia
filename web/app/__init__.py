from ntpath import join
from posixpath import dirname
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_talisman import Talisman
from app.config import Config
from pathlib import Path

db = SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

def create_app():
    app = Flask(__name__)

    # TODO: Configure CSP with Talisman

    # Load environment variables from file
    # With PurePath objects the slash operator is overidden to create child paths, similarly to os.path.join()
    env_path = Path('.')/'env.dev'
    load_dotenv(dotenv_path=env_path, override=True)

    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    login_manager.init_app(app)

    from app.main.routes import main
    from app.users.routes import users
    from app.errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(errors)
    
    return app