from app.helpers.application import app
from app.helpers.database import db, ma
from app.helpers.logging import logger


def create_app():

    from app import models

    with app.app_context():
        db.create_all()

    logger.info("Aplicacao iniciada com sucesso.")

    from app.resources.produtor_resource import produtor_bp
    from app.resources.propriedade_resource import propriedade_bp
    from app.resources.cultura_resource import cultura_bp

    app.register_blueprint(produtor_bp)
    app.register_blueprint(propriedade_bp)
    app.register_blueprint(cultura_bp)

    return app
