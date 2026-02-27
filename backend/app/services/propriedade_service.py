from app.helpers.logging import logger
from app.repositories.propriedade_repository import PropriedadeRepository


class PropriedadeService:

    @staticmethod
    def listar(nome, produtor_id, page, per_page):
        logger.info("Listando propriedades | filtros aplicados")
        return PropriedadeRepository.find_filtered(nome, produtor_id, page, per_page)

    @staticmethod
    def buscar_por_id(id):
        logger.info(f"Buscando propriedade ID {id}")
        return PropriedadeRepository.find_by_id(id)

    @staticmethod
    def salvar(propriedade):
        logger.info("Salvando propriedade")
        return PropriedadeRepository.save(propriedade)

    @staticmethod
    def deletar(propriedade):
        logger.warning(f"Removendo propriedade {propriedade.id}")
        PropriedadeRepository.delete(propriedade)
