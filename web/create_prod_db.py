from app import db, models
from run import app

with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.commit()