up:
	docker-compose up
	make admin
	make static

dev-up:
	docker-compose -f docker-compose.dev.yml up
	make admin
	make static

down:
	docker-compose down -v

admin:
	docker-compose exec mailer_panel python manage.py createsuperuser --username admin --email admin@email.com --no-input

static:
	docker-compose exec mailer_panel python manage.py collectstatic --no-input --clear