from app import db

class Propriedade(db.Model):
    __tablename__ = "propriedades"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tamanho_hectares = db.Column(db.Float, nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(50), nullable=False)

    produtor_id = db.Column(db.Integer, db.ForeignKey("produtores.id"), nullable=False)

    culturas = db.relationship("Cultura", backref="propriedade", lazy=True)