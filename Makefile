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
BOT_FILE = docker_compose/bot.yml
BOT_CONTAINER = bot
BOT_SERVICE_FILE = docker_compose/bot_service.yml
BOT_SERVICE_CONTAINER = bot_service


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
	$(DC) -f $(APP_FILE) $(ENV) -f $(DB_FILE) $(ENV) -f $(BOT_FILE) -f $(BOT_SERVICE_FILE) up --build -d

.PHONY: all-down
all-down:
	$(DC) -f $(APP_FILE) $(ENV) -f $(DB_FILE) $(ENV) -f $(BOT_FILE) -f $(BOT_SERVICE_FILE) down


.PHONY: bot
bot:
	$(DC) -f $(BOT_FILE) up --build -d

.PHONY: bot-down
bot-down:
	$(DC) -f $(BOT_FILE) down

.PHONY: bot-logs
bot-logs:
	$(LOGS) $(BOT_CONTAINER) -f

.PHONY: bot-shell
bot-shell:
	$(EXEC) $(BOT_CONTAINER) bash

.PHONY: bot_service
bot_service:
	$(DC) -f $(BOT_SERVICE_FILE) up --build -d

.PHONY: bot_service-down
bot_service-down:
	$(DC) -f $(BOT_SERVICE_FILE) down

.PHONY: bot_service-logs
bot_service-logs:
	$(LOGS) $(BOT_SERVICE_CONTAINER) -f

.PHONY: bot_serivce-shell
bot_service-shell:
	$(EXEC) $(BOT_SERVICE_CONTAINER) bash