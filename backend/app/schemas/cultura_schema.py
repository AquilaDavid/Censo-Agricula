# app/schemas/cultura_schema.py
from app import ma
from app.models.cultura import Cultura

class CulturaSchema(ma.SQLAlchemyAutoSchema):
    
    propriedade = ma.Nested('PropriedadeSchema', only=('id', 'nome', 'cidade'))

    class Meta:
        model = Cultura
        load_instance = True
        include_fk = True

cultura_schema = CulturaSchema()
culturas_schema = CulturaSchema(many=True)