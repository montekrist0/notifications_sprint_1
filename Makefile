up:
	docker-compose up
	docker-compose exec mailer_panel python manage.py createsuperuser --username admin --email admin@email.com --no-input
down:
	docker-compose down -v

admin:
	docker-compose exec mailer_panel python manage.py createsuperuser --username admin --email admin@email.com --no-input