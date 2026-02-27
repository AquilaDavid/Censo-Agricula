from app.helpers.logging import logger
from app.repositories.produtor_repository import ProdutorRepository


class ProdutorService:

    @staticmethod
    def listar(nome, idade, page, per_page):
        logger.info("Listando produtores | filtros aplicados")
        return ProdutorRepository.find_filtered(nome, idade, page, per_page)

    @staticmethod
    def buscar_por_id(id):
        logger.info(f"Buscando produtor ID {id}")
        return ProdutorRepository.find_by_id(id)

    @staticmethod
    def salvar(produtor):
        logger.info("Salvando produtor")
        return ProdutorRepository.save(produtor)

    @staticmethod
    def deletar(produtor):
        logger.warning(f"Removendo produtor {produtor.id}")
        ProdutorRepository.delete(produtor)
