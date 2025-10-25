.PHONY: up down logs run bash init reset

up:
	docker compose up -d --build

down:
	docker compose down

logs:
	docker compose logs -f --tail=200

run:
	docker compose run --rm dlt-runner

bash:
	docker compose run --rm dlt-runner bash

init-db:
	# Wait for Postgres to be healthy and show databases
	docker compose exec -T postgres psql -U $${POSTGRES_USER:-dlt} -d $${POSTGRES_DB:-dlt} -c '\l'

reset:
	docker compose down -v
	rm -rf .dlt
