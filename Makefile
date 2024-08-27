DC = docker compose
DB_CONTAINER = pg_db
FASTAPI_APP = src.main:app
EXEC = docker exec -it
A_MIG = alembic revision --autogenerate
A_UPG = alembic upgrade head

db:
	$(DC) up -d

db-down:
	$(DC) down

db-logs:
	$(DC) logs

mg:
	$(A_MIG)

upg:
	$(A_UPG)

app:
	uvicorn $(FASTAPI_APP) --reload
