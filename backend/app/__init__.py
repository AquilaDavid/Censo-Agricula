from flask import Flask
from app.config import Config
from app.helpers.database import db, ma
from app.helpers.logging import logger

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        from app import models
        db.create_all()

    logger.info("Aplicacao iniciada com sucesso.")

    from app.resources.produtor_resource import produtor_bp
    from app.resources.propriedade_resource import propriedade_bp
    from app.resources.cultura_resource import cultura_bp

    app.register_blueprint(produtor_bp)
    app.register_blueprint(propriedade_bp)
    app.register_blueprint(cultura_bp)

    return app