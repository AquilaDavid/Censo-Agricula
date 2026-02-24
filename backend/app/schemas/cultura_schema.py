from app import ma
from app.models.cultura import Cultura

class CulturaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cultura
        load_instance = True

cultura_schema = CulturaSchema()
culturas_schema = CulturaSchema(many=True)