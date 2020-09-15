# Develop Machine
build-dev:
	docker-compose -f docker-compose.dev.yml build --no-cache

run-dev:
	docker-compose -f docker-compose.dev.yml up --scale celery_worker=3

down-dev:
	docker-compose -f docker-compose.dev.yml down

# Raspberry Pi
build-pi:
	docker-compose -f docker-compose.pi.yml build --no-cache

run-pi:
	docker-compose -f docker-compose.pi.yml up --scale celery_worker=3

down-pi:
	docker-compose -f docker-compose.pi.yml down

# Sonarqube
build-sq:
	docker-compose -f docker-compose.sonarqube.yml build --no-cache sonarqube

run-ss:
	docker-compose -f docker-compose.sonarqube.yml up sonarqube

build-ss:
	docker-compose -f docker-compose.sonarqube.yml build --no-cache sonar-scanner

run-ss:
	docker-compose -f docker-compose.sonarqube.yml up sonar-scanner