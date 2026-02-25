from flask import Blueprint

# TODO: implementar CRUD completo da Cultura (Futuro desenvolvimento)
cultura_bp = Blueprint("cultura_bp", __name__, url_prefix="/culturas")


@cultura_bp.route("", methods=["GET"])
def listar_culturas():
    return {"data": [], "message": "Endpoint de culturas em desenvolvimento"}