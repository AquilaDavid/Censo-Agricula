from flask import Flask
from app.helpers.database import db, ma
from app.helpers.logging import logger

from app import models
from app.config import Config

from app.resources.produtor_resource import produtor_bp
from app.resources.propriedade_resource import propriedade_bp
from app.resources.cultura_resource import cultura_bp

def create_app():
    
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        db.create_all()

    logger.info("Aplicacao iniciada com sucesso.")
    
    app.register_blueprint(produtor_bp)
    app.register_blueprint(propriedade_bp)
    app.register_blueprint(cultura_bp)

    return app
