BACKEND_PATH = backend
DJANGO_CMD = python $(BACKEND_PATH)/manage.py
SETTINGS = point_of_sale.settings

# BACKEND COMMANDS
migrations:
	$(DJANGO_CMD) makemigrations api

migrate:
	$(DJANGO_CMD) migrate api

create-superuser:
	$(DJANGO_CMD) createsuperuser

shell:
	$(DJANGO_CMD) shell --settings=$(SETTINGS)

runserver:
	$(DJANGO_CMD) runserver 0.0.0.0:8000 --settings=$(SETTINGS)

test:
	$(DJANGO_CMD) test $(BACKEND_PATH) --settings=$(SETTINGS)

collectstatic:
	$(DJANGO_CMD) collectstatic --noinput

install_dev:
	pip install -r $(BACKEND_PATH)/point_of_sale/requirements/dev_requirements.txt 

install_prod:
	pip install -r $(BACKEND_PATH)/point_of_sale/requirements/prod_requirements.txt

local_start: install_dev migrations migrate

prod_start: install_prod migrations migrate collectstatic runserver

load_fixture_docker:
	docker-compose exec backend $(DJANGO_CMD) loaddata backend/point_of_sale/fixtures/db.json

load_fixture:
	$(DJANGO_CMD) loaddata backend/point_of_sale/fixtures/db.json