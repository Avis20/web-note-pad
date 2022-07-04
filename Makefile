.DEFAULT_GOAL := help

.PHONY: black
black: ## Autoformat code by black
	black .

.PHONY: build
build: ## Build images
	docker-compose -f docker-compose.yml -f docker-compose.override.yml build

.PHONY: up
up: ## Up all services locally with docker-compose
	touch .env
	docker-compose up

.PHONY: down
down: ## Down all services locally with docker-compose as daemon
	docker-compose down

uninstall: ## Complete remove containers and named volumes
	docker-compose down --remove-orphans --volumes

.PHONY: run_tests
run_tests: ## Run tests in docker-compose
	touch .env
	docker-compose -f docker-compose.yml -f docker-compose.override.yml -f docker-compose.test.yml run doc-backend

.PHONY: lint
lint: flake8

.PHONY: help
help: ## Help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
