from app import create_app, db
from app.models.produtor import Produtor
from app.models.propriedade import Propriedade
from app.models.cultura import Cultura

app = create_app()  # se você tiver uma factory function

with app.app_context():  # ✅ aqui entra o contexto do Flask
    # Limpar tabelas (opcional)
    Cultura.query.delete()
    Propriedade.query.delete()
    Produtor.query.delete()
    db.session.commit()

    # Criar produtores
    produtores = [
        Produtor(id=1, nome="João Silva", cpf="111.111.111-11", idade=45),
        Produtor(id=2, nome="Maria Oliveira", cpf="222.222.222-22", idade=38),
        Produtor(id=3, nome="Carlos Santos", cpf="333.333.333-33", idade=50),
        Produtor(id=4, nome="Ana Souza", cpf="444.444.444-44", idade=42),
        Produtor(id=5, nome="Pedro Lima", cpf="555.555.555-55", idade=35),
        Produtor(id=6, nome="Juliana Costa", cpf="666.666.666-66", idade=29),
        Produtor(id=7, nome="Rafael Alves", cpf="777.777.777-77", idade=55),
        Produtor(id=8, nome="Camila Rocha", cpf="888.888.888-88", idade=33),
        Produtor(id=9, nome="Lucas Pereira", cpf="999.999.999-99", idade=41),
        Produtor(id=10, nome="Fernanda Martins", cpf="000.000.000-00", idade=36),
    ]
    db.session.add_all(produtores)
    db.session.commit()

    # Criar propriedades
    propriedades = [
        Propriedade(id=1, nome="Fazenda Boa Vista", tamanho_hectares=120.5, cidade="Campina Grande", estado="PB", produtor_id=1),
        Propriedade(id=2, nome="Sítio Verde", tamanho_hectares=80.0, cidade="Patos", estado="PB", produtor_id=2),
        Propriedade(id=3, nome="Chácara Feliz", tamanho_hectares=50.2, cidade="Sousa", estado="PB", produtor_id=3),
        Propriedade(id=4, nome="Fazenda Horizonte", tamanho_hectares=200.0, cidade="Pombal", estado="PB", produtor_id=4),
        Propriedade(id=5, nome="Sítio do Sol", tamanho_hectares=75.0, cidade="Itaporanga", estado="PB", produtor_id=5),
        Propriedade(id=6, nome="Fazenda Nova Era", tamanho_hectares=150.0, cidade="Queimadas", estado="PB", produtor_id=6),
        Propriedade(id=7, nome="Chácara Primavera", tamanho_hectares=60.0, cidade="Campina Grande", estado="PB", produtor_id=7),
        Propriedade(id=8, nome="Sítio das Flores", tamanho_hectares=90.0, cidade="Patos", estado="PB", produtor_id=8),
        Propriedade(id=9, nome="Fazenda Paraíso", tamanho_hectares=180.0, cidade="Sousa", estado="PB", produtor_id=9),
        Propriedade(id=10, nome="Chácara Alegre", tamanho_hectares=55.0, cidade="Pombal", estado="PB", produtor_id=10),
    ]
    db.session.add_all(propriedades)
    db.session.commit()

    # Criar culturas
    culturas = [
        Cultura(id=1, nome_cultura="Milho", area_plantada=20.0, propriedade_id=1),
        Cultura(id=2, nome_cultura="Soja", area_plantada=35.0, propriedade_id=2),
        Cultura(id=3, nome_cultura="Feijão", area_plantada=15.0, propriedade_id=3),
        Cultura(id=4, nome_cultura="Trigo", area_plantada=50.0, propriedade_id=4),
        Cultura(id=5, nome_cultura="Cana-de-açúcar", area_plantada=40.0, propriedade_id=5),
        Cultura(id=6, nome_cultura="Algodão", area_plantada=30.0, propriedade_id=6),
        Cultura(id=7, nome_cultura="Tomate", area_plantada=10.0, propriedade_id=7),
        Cultura(id=8, nome_cultura="Batata", area_plantada=25.0, propriedade_id=8),
        Cultura(id=9, nome_cultura="Cenoura", area_plantada=12.0, propriedade_id=9),
        Cultura(id=10, nome_cultura="Laranja", area_plantada=18.0, propriedade_id=10),
    ]
    db.session.add_all(culturas)
    db.session.commit()

    print("Banco populado com sucesso! ✅")