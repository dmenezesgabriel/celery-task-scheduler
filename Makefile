# Develop Machine
build-dev:
	time docker-compose -f docker-compose.dev.yml build

run-dev:
	docker-compose -f docker-compose.dev.yml up -d --scale celery_worker=3

down-dev:
	docker-compose -f docker-compose.dev.yml down

# Raspberry pi
build-pi:
	time docker-compose -f docker-compose.pi.yml build

run-pi:
	docker-compose -f docker-compose.pi.yml up --scale celery_worker=3

down-pi:
	docker-compose -f docker-compose.pi.yml down

# Sonarqube
build-sq:
	docker-compose -f docker-compose.sonarqube.yml build sonarqube

run-ss:
	docker-compose -f docker-compose.sonarqube.yml up sonarqube

build-ss:
	docker-compose -f docker-compose.sonarqube.yml build sonar-scanner

run-ss:
	docker-compose -f docker-compose.sonarqube.yml up sonar-scanner