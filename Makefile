BACKEND_PATH = backend
DJANGO_CMD = python $(BACKEND_PATH)/manage.py
SETTINGS = point_of_sale.settings

migrations:
	$(DJANGO_CMD) makemigrations

migrate:
	$(DJANGO_CMD) migrate

create-superuser:
	$(DJANGO_CMD) createsuperuser

shell:
	$(DJANGO_CMD) shell --settings=$(SETTINGS)

runserver:
	$(DJANGO_CMD) runserver 0.0.0.0:8000 --settings=$(SETTINGS)

test:
	$(DJANGO_CMD) test $(BACKEND_PATH) --settings=$(SETTINGS)