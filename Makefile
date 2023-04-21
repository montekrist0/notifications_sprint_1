up-dev:
	docker-compose -f docker-compose.dev.yml up
re-build:
	docker-compose -f docker-compose.dev.yml stop
	docker-compose -f docker-compose.dev.yml down
	make up-dev
re-build-app-dev:
	docker-compose -f docker-compose.dev.yml up --build --no-deps -d notification_app