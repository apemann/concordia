from ntpath import join
from posixpath import dirname
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.config import Config
from pathlib import Path

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Load environment variables from file
    # With PurePath objects the slash operator is overidden to create child paths, similarly to os.path.join()
    env_path = Path('.')/'env.dev'
    load_dotenv(dotenv_path=env_path, override=True)

    app.config.from_object(Config)
    db.init_app(app)

    login_manager.init_app(app)

    from app.routes import main
    app.register_blueprint(main)
    
    return app