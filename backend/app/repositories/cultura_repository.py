from app.models.cultura import Cultura


class CulturaRepository:

    @staticmethod
    def save(cultura):
        from app.helpers.database import db
        db.session.add(cultura)
        db.session.commit()
        return cultura

    @staticmethod
    def find_by_id(id):
        return Cultura.query.get(id)

    @staticmethod
    def delete(cultura):
        from app.helpers.database import db
        db.session.delete(cultura)
        db.session.commit()

    @staticmethod
    def find_filtered(nome_cultura=None, propriedade_id=None, page=1, per_page=5):
        query = Cultura.query

        if nome_cultura:
            query = query.filter(Cultura.nome_cultura.ilike(f"%{nome_cultura}%"))

        if propriedade_id:
            query = query.filter(Cultura.propriedade_id == propriedade_id)

        return query.paginate(page=page, per_page=per_page, error_out=False)
