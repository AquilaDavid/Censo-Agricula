from app.helpers.logging import logger
from app.repositories.cultura_repository import CulturaRepository


class CulturaService:

    @staticmethod
    def listar(nome_cultura, propriedade_id, page, per_page):
        logger.info("Listando culturas | filtros aplicados")
        return CulturaRepository.find_filtered(nome_cultura, propriedade_id, page, per_page)

    @staticmethod
    def buscar_por_id(id):
        logger.info(f"Buscando cultura ID {id}")
        return CulturaRepository.find_by_id(id)

    @staticmethod
    def salvar(cultura):
        logger.info("Salvando cultura")
        return CulturaRepository.save(cultura)

    @staticmethod
    def deletar(cultura):
        logger.warning(f"Removendo cultura {cultura.id}")
        CulturaRepository.delete(cultura)
