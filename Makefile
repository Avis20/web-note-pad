
BASE_DOCKER_COMPOSES = -f docker-compose.yml
ENV_FILE = --env-file ./.docker.env

create_network:
	@docker network create web-notepad-network 2>/dev/null || echo "web-notepad-network is up-to-date"


# prod start
.PHONY: up
up: create_network ## up services
	@docker-compose $(ENV_FILE) $(BASE_DOCKER_COMPOSES) up -d

.PHONY: logs
logs: ## tail logs services
	@docker-compose $(ENV_FILE) $(BASE_DOCKER_COMPOSES) logs -f

.PHONY: down
down: ## down services
	@docker-compose $(ENV_FILE) $(BASE_DOCKER_COMPOSES) down

.PHONY: build
build: ## build services
# make build service=web_notepad_backend
	@docker-compose $(ENV_FILE) $(BASE_DOCKER_COMPOSES) build $(service)

.PHONY: restart
restart: down up ## restart services

.PHONY: uninstall
uninstall: ## uninstall all services
	@docker-compose $(ENV_FILE) $(BASE_DOCKER_COMPOSES) down --remove-orphans --volumes
# prod end
