VENV = venv
BACKEND = backend
DATA_COLLECTOR = data_collector
FRONTEND = frontend

VENV_BACKEND = $(BACKEND)/$(VENV)
VENV_DATA_COLLECTOR = $(DATA_COLLECTOR)/$(VENV)

PYTHON_VERSION = 3.9
SYSTEM_PYTHON = $(shell which python$(PYTHON_VERSION))

VENV_ACTIVATE_BACKEND = . $(VENV_BACKEND)/bin/activate
VENV_ACTIVATE_DATA_COLLECTOR = . $(VENV_DATA_COLLECTOR)/bin/activate

PYTHON_BACKEND = $(VENV_BACKEND)/bin/python3
PYTHON_DATA_COLLECTOR = $(VENV_DATA_COLLECTOR)/bin/python3

ENV_VARS = set -o allexport; . $(BACKEND)/.env; set +o allexport

PIP_BACKEND = $(VENV_BACKEND)/bin/pip
PIP_DATA_COLLECTOR = $(VENV_DATA_COLLECTOR)/bin/pip

venv:
	test -d $(VENV_BACKEND) || $(SYSTEM_PYTHON) -m venv $(VENV_BACKEND)
	test -d $(VENV_DATA_COLLECTOR) || $(SYSTEM_PYTHON) -m venv $(VENV_DATA_COLLECTOR)

install: venv
	$(VENV_ACTIVATE_BACKEND) && $(PIP_BACKEND) install -r $(BACKEND)/requirements.txt
	$(VENV_ACTIVATE_DATA_COLLECTOR) && $(PIP_DATA_COLLECTOR) install -r $(DATA_COLLECTOR)/requirements.txt

install-dev: install
	$(VENV_ACTIVATE_BACKEND) && $(PIP_BACKEND) install -r $(BACKEND)/requirements_dev.txt
	$(VENV_ACTIVATE_DATA_COLLECTOR) && $(PIP_DATA_COLLECTOR) install -r $(DATA_COLLECTOR)/requirements_dev.txt

install-ui:
	npm install --prefix $(FRONTEND)

lint:
	$(VENV_ACTIVATE_BACKEND) && $(VENV_BACKEND)/bin/pylint --rcfile=$(BACKEND)/.pylintrc $(BACKEND)/config.py $(BACKEND)/wsgi.py $(BACKEND)/application/
	$(VENV_ACTIVATE_DATA_COLLECTOR) && $(VENV_DATA_COLLECTOR)/bin/pylint --rcfile=$(DATA_COLLECTOR)/.pylintrc $(DATA_COLLECTOR)/data_collector.py

lint-ui:
	npm run --prefix $(FRONTEND) lint

flake8:
	$(VENV_ACTIVATE_BACKEND) && $(VENV_BACKEND)/bin/flake8 --config=$(BACKEND)/.flake8 $(BACKEND)/config.py $(BACKEND)/wsgi.py $(BACKEND)/application/
	$(VENV_ACTIVATE_DATA_COLLECTOR) && $(VENV_DATA_COLLECTOR)/bin/flake8 --config=$(DATA_COLLECTOR)/.flake8 $(DATA_COLLECTOR)/data_collector.py

testing:
	$(VENV_ACTIVATE_BACKEND) && $(VENV_BACKEND)/bin/pytest --cov=$(BACKEND)/application $(BACKEND)/tests/

testing-ui:
	npm run --prefix $(FRONTEND) test:unit

checking: lint flake8 testing lint-ui testing-ui

create-env:
ifeq ($(shell test -s $(BACKEND)/.env && echo -n 0), 0)
	@echo 'Skipping this step - backend/.env file exists.'
else
	cp $(BACKEND)/.env.example $(BACKEND)/.env
	$(VENV_ACTIVATE_BACKEND) && $(PYTHON_BACKEND) -c 'import os; print("SECRET_KEY={}".format(os.urandom(24)))' >> $(BACKEND)/.env
endif

create-config:
ifeq ($(shell test -s $(BACKEND)/data-usage-monitor.ini && echo -n 0), 0)
	@echo 'Skipping this step - backend/data-usage-monitor.ini file exists.'
else
	cp data-usage-monitor.ini.example $(BACKEND)/data-usage-monitor.ini
endif
ifeq ($(shell test -s $(DATA_COLLECTOR)/data-usage-monitor.ini && echo -n 0), 0)
	@echo 'Skipping this step - data_collector/data-usage-monitor.ini file exists.'
else
	cp data-usage-monitor.ini.example $(DATA_COLLECTOR)/data-usage-monitor.ini
endif

prepare: prepare-deps prepare-env

prepare-deps: install install-ui

prepare-env: create-env create-config

upgrade-db:
	$(VENV_ACTIVATE_BACKEND) && $(ENV_VARS) && $(VENV_BACKEND)/bin/flask db upgrade --directory $(BACKEND)/migrations

downgrade-db:
	$(VENV_ACTIVATE_BACKEND) && $(ENV_VARS) && $(VENV_BACKEND)/bin/flask db downgrade base --directory $(BACKEND)/migrations

reset-db: downgrade-db upgrade-db

run-flask:
	$(VENV_ACTIVATE_BACKEND) && $(ENV_VARS) && $(VENV_BACKEND)/bin/flask run

run-uwsgi:
	$(VENV_ACTIVATE_BACKEND) && $(VENV_BACKEND)/bin/uwsgi --ini $(BACKEND)/data-usage-monitor.ini

run-data-collector:
	$(VENV_ACTIVATE_DATA_COLLECTOR) && $(PYTHON_DATA_COLLECTOR) $(DATA_COLLECTOR)/data_collector.py

run-ui:
	export VUE_APP_USE_MOCKED_VALUES=false && npm run --prefix $(FRONTEND) serve

run-ui-mock:
	export VUE_APP_USE_MOCKED_VALUES=true && npm run --prefix $(FRONTEND) serve

build-docker:
	$(ENV_VARS) && docker-compose build

build-docker-mock:
	$(ENV_VARS) && docker-compose build --build-arg MOCKED_VALUES=true

run-docker:
	$(ENV_VARS) && export POSTGRES_HOST=db && docker-compose up -d

stop-docker:
	$(ENV_VARS) && docker-compose stop

clean-docker:
	$(ENV_VARS) && docker-compose down --rmi=all --volume

clean:
	rm -rf __pycache__
	rm -rf $(VENV)
	rm -rf $(DATA_COLLECTOR)/__pycache__
	rm -rf $(DATA_COLLECTOR)/data-usage-monitor.ini
	rm -rf $(VENV_DATA_COLLECTOR)
	rm -rf $(BACKEND)/__pycache__
	rm -rf $(BACKEND)/data-usage-monitor.ini
	rm -rf $(BACKEND)/.env
	rm -rf $(VENV_BACKEND)
	rm -rf $(FRONTEND)/node_modules
	
.PHONY: venv install install-dev install-ui lint lint-ui flake8 testing testing-ui checking create-env create-config copy-config prepare prepare-deps prepare-env upgrade-db run-app run-data-collector run-ui run-ui-mock build-docker build-docker-mock run-docker stop-docker clean-docker clean
