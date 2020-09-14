build-dev:
	docker-compose -f docker-compose.dev.yml build --no-cache

run-dev:
	docker-compose -f docker-compose.dev.yml up --scale celery_worker=3

down-dev:
	docker-compose -f docker-compose.dev.yml down

