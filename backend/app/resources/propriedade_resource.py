import json

from app.helpers.redis import redis_client
from app.helpers.cache import gerar_chave_cache
from app.config import Config

from flask import Blueprint, request
from app.schemas.propriedade_schema import propriedade_schema, propriedades_schema
from app.services.propriedade_service import PropriedadeService

propriedade_bp = Blueprint("propriedade_bp", __name__, url_prefix="/propriedades")


@propriedade_bp.route("", methods=["GET"])
def listar_propriedades():

    nome = request.args.get("nome")
    produtor_id = request.args.get("produtor_id", type=int)
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 5, type=int)

    cache_key = gerar_chave_cache(
        "propriedades",
        f"{nome}:{produtor_id}:{page}:{per_page}"
    )

    cached_data = redis_client.get(cache_key)

    if cached_data:
        return json.loads(cached_data)

    pagination = PropriedadeService.listar(
        nome,
        produtor_id,
        page,
        per_page
    )

    result = {
        "data": propriedades_schema.dump(pagination.items),
        "pagination": {
            "total": pagination.total,
            "page": pagination.page,
            "pages": pagination.pages,
            "per_page": per_page
        }
    }

    redis_client.setex(
        cache_key,
        Config.CACHE_TTL,
        json.dumps(result)
    )

    return result


@propriedade_bp.route("/<int:id>", methods=["GET"])
def buscar_propriedade(id):

    cache_key = f"propriedade:{id}"

    cached_data = redis_client.get(cache_key)

    if cached_data:
        return json.loads(cached_data)

    propriedade = PropriedadeService.buscar_por_id(id)

    if not propriedade:
        return {"message": "Propriedade nao encontrada"}, 404

    result = {
        "data": propriedade_schema.dump(propriedade),
        "links": {
            "self": f"/propriedades/{id}",
            "produtor": f"/produtores/{propriedade.produtor_id}"
        }
    }

    redis_client.setex(
        cache_key,
        Config.CACHE_TTL,
        json.dumps(result)
    )

    return result


@propriedade_bp.route("", methods=["POST"])
def criar_propriedade():

    propriedade = propriedade_schema.load(request.json)
    propriedade = PropriedadeService.salvar(propriedade)

    redis_client.delete(f"propriedade:{propriedade.id}")

    for key in redis_client.scan_iter("propriedades:*"):
        redis_client.delete(key)

    return {
        "data": propriedade_schema.dump(propriedade),
        "message": "Propriedade criada com sucesso"
    }, 201


@propriedade_bp.route("/<int:id>", methods=["PUT"])
def atualizar_propriedade(id):

    propriedade = PropriedadeService.buscar_por_id(id)

    if not propriedade:
        return {"message": "Propriedade nao encontrada"}, 404

    data = request.json

    propriedade.nome = data["nome"]
    propriedade.tamanho_hectares = data["tamanho_hectares"]
    propriedade.municipio_nome = data["municipio_nome"]
    propriedade.municipio_codigo = data["municipio_codigo"]
    propriedade.estado_nome = data["estado_nome"]
    propriedade.estado_uf = data["estado_uf"]
    propriedade.produtor_id = data["produtor_id"]

    PropriedadeService.salvar(propriedade)

    redis_client.delete(f"propriedade:{id}")

    for key in redis_client.scan_iter("propriedades:*"):
        redis_client.delete(key)

    return {
        "data": propriedade_schema.dump(propriedade)
    }


@propriedade_bp.route("/<int:id>", methods=["PATCH"])
def atualizar_parcial(id):

    propriedade = PropriedadeService.buscar_por_id(id)

    if not propriedade:
        return {"message": "Propriedade nao encontrada"}, 404

    data = request.json

    if "nome" in data:
        propriedade.nome = data["nome"]

    if "tamanho_hectares" in data:
        propriedade.tamanho_hectares = data["tamanho_hectares"]

    if "municipio_nome" in data:
        propriedade.municipio_nome = data["municipio_nome"]

    if "municipio_codigo" in data:
        propriedade.municipio_codigo = data["municipio_codigo"]

    if "estado_nome" in data:
        propriedade.estado_nome = data["estado_nome"]

    if "estado_uf" in data:
        propriedade.estado_uf = data["estado_uf"]

    if "produtor_id" in data:
        propriedade.produtor_id = data["produtor_id"]

    PropriedadeService.salvar(propriedade)

    redis_client.delete(f"propriedade:{id}")

    for key in redis_client.scan_iter("propriedades:*"):
        redis_client.delete(key)

    return {
        "data": propriedade_schema.dump(propriedade)
    }


@propriedade_bp.route("/<int:id>", methods=["DELETE"])
def deletar_propriedade(id):

    propriedade = PropriedadeService.buscar_por_id(id)

    if not propriedade:
        return {"message": "Propriedade nao encontrada"}, 404

    redis_client.delete(f"propriedade:{id}")

    for key in redis_client.scan_iter("propriedades:*"):
        redis_client.delete(key)

    PropriedadeService.deletar(propriedade)

    return {}, 204