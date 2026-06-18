import json

from app.helpers.redis import redis_client
from app.helpers.cache import gerar_chave_cache
from app.config import Config

from flask import Blueprint, request
from app.schemas.produtor_schema import produtor_schema, produtores_schema
from app.services.produtor_service import ProdutorService

produtor_bp = Blueprint("produtor_bp", __name__, url_prefix="/produtores")


@produtor_bp.route("", methods=["GET"])
def listar_produtores():

    nome = request.args.get("nome")
    idade = request.args.get("idade", type=int)
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 5, type=int)

    cache_key = gerar_chave_cache(
        "produtores",
        f"{nome}:{idade}:{page}:{per_page}"
    )

    cached_data = redis_client.get(cache_key)

    if cached_data:
        return json.loads(cached_data)

    pagination = ProdutorService.listar(
        nome,
        idade,
        page,
        per_page
    )

    result = {
        "data": produtores_schema.dump(pagination.items),
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


@produtor_bp.route("/<int:id>", methods=["GET"])
def buscar_produtor(id):

    cache_key = f"produtor:{id}"

    cached_data = redis_client.get(cache_key)

    if cached_data:
        return json.loads(cached_data)

    produtor = ProdutorService.buscar_por_id(id)

    if not produtor:
        return {"message": "Produtor nao encontrado"}, 404

    result = {
        "data": produtor_schema.dump(produtor),
        "links": {
            "self": f"/produtores/{id}",
            "propriedades": f"/produtores/{id}/propriedades"
        }
    }

    redis_client.setex(
        cache_key,
        Config.CACHE_TTL,
        json.dumps(result)
    )

    return result


@produtor_bp.route("", methods=["POST"])
def criar_produtor():

    produtor = produtor_schema.load(request.json)
    produtor = ProdutorService.salvar(produtor)

    redis_client.delete(f"produtor:{produtor.id}")

    for key in redis_client.scan_iter("produtores:*"):
        redis_client.delete(key)

    return {
        "data": produtor_schema.dump(produtor),
        "message": "Produtor criado com sucesso"
    }, 201


@produtor_bp.route("/<int:id>", methods=["PUT"])
def atualizar_produtor(id):

    produtor = ProdutorService.buscar_por_id(id)

    if not produtor:
        return {"message": "Produtor nao encontrado"}, 404

    data = request.json

    produtor.nome = data["nome"]
    produtor.cpf = data["cpf"]
    produtor.data_nascimento = data["data_nascimento"]

    ProdutorService.salvar(produtor)

    redis_client.delete(f"produtor:{id}")

    for key in redis_client.scan_iter("produtores:*"):
        redis_client.delete(key)

    return {
        "data": produtor_schema.dump(produtor)
    }


@produtor_bp.route("/<int:id>", methods=["PATCH"])
def atualizar_parcial(id):

    produtor = ProdutorService.buscar_por_id(id)

    if not produtor:
        return {"message": "Produtor nao encontrado"}, 404

    data = request.json

    if "nome" in data:
        produtor.nome = data["nome"]

    if "cpf" in data:
        produtor.cpf = data["cpf"]

    if "data_nascimento" in data:
        produtor.data_nascimento = data["data_nascimento"]

    ProdutorService.salvar(produtor)

    redis_client.delete(f"produtor:{id}")

    for key in redis_client.scan_iter("produtores:*"):
        redis_client.delete(key)

    return {
        "data": produtor_schema.dump(produtor)
    }


@produtor_bp.route("/<int:id>", methods=["DELETE"])
def deletar_produtor(id):

    produtor = ProdutorService.buscar_por_id(id)

    if not produtor:
        return {"message": "Produtor nao encontrado"}, 404

    redis_client.delete(f"produtor:{id}")

    for key in redis_client.scan_iter("produtores:*"):
        redis_client.delete(key)

    ProdutorService.deletar(produtor)

    return {}, 204