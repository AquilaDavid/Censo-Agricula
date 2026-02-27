# React + Flask SOLID Architecture

Frontend: ReactJS
Backend: Flask (Clean Architecture + SOLID)
Database: PostgreSQL

Tema: Censo Agrícola

Equipe: Áquila, Pedro Gabriel Mandu dos Santos, Juliene Barbosa da Silva e Maria José de Souza Gonçalves


# Instuções para o Docker:

docker run --name CensoAgricula -e POSTGRES_PASSWORD=123456 -e POSTGRES_USER=censoAgricula -e POSTGRES_DB=censo -p 5434:5432 postgres:18.1-alpine3.22

docker start CensoAgricula

docker exec -it CensoAgricula psql -U censoAgricula -d censo

Ao fechar o Banco
docker stop CensoAgricula

