DC = docker compose
DB_FILE = docker_compose/storage.yml
DB_CONTAINER = pg_db
APP_FILE = docker_compose/app.yml
APP_CONTAINER = main-app
EXEC = docker exec -it
MG= alembic revision --autogenerate
UPG = alembic upgrade head
ENV = --env-file .env
LOGS = docker logs


.PHONY: storage
storage:
	$(DC) -f $(DB_FILE) $(ENV) up -d

.PHONY: storage-down
storage-down:
	$(DC) -f $(DB_FILE) $(ENV) down

.PHONY: storage-logs
storage-logs:
	$(LOGS) $(DB_CONTAINER) -f

.PHONY: app
app:
	$(DC) -f $(APP_FILE) $(ENV) up --build -d

.PHONY: app-down
app-down:
	$(DC) -f $(APP_FILE) $(ENV)  down

.PHONY: app-logs
app-logs:
	$(LOGS) $(APP_CONTAINER) -f

.PHONY: migrations
migrations:
	$(EXEC) $(APP_CONTAINER) $(MG)


.PHONY: migrate
migrate:
	$(EXEC) $(APP_CONTAINER) $(UPG)

.PHONY: all
all:
	$(DC) -f $(APP_FILE) $(ENV) -f $(DB_FILE) $(ENV) up --build -d

.PHONY: all-down
all-down:
	$(DC) -f $(APP_FILE) $(ENV) -f $(DB_FILE) $(ENV) down




