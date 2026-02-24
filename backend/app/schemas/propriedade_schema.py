from app import ma
from app.models.propriedade import Propriedade

class PropriedadeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Propriedade
        load_instance = True

propriedade_schema = PropriedadeSchema()
propriedades_schema = PropriedadeSchema(many=True)