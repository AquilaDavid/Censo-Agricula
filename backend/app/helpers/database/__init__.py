from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app.helpers.application import app

db = SQLAlchemy()
ma = Marshmallow()

db.init_app(app)
ma.init_app(app)
