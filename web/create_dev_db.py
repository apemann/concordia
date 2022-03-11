from app import db, models
from run import app

with app.app_context():
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@0.0.0.0:5432/site_db"
    db.drop_all()
    db.create_all()
    db.session.commit()