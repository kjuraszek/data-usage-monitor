VENV = venv
DATA_COLLECTOR = data_collector
VENV_DATA_COLLECTOR = $(DATA_COLLECTOR)/venv
PYTHON_VERSION = 3.9
SYSTEM_PYTHON = $(shell which python$(PYTHON_VERSION))
PYTHON = $(VENV)/bin/python3
PYTHON_DATA_COLLECTOR = $(VENV_DATA_COLLECTOR)/bin/python3
PIP = $(VENV)/bin/pip
PIP_DATA_COLLECTOR = $(VENV_DATA_COLLECTOR)/bin/pip
FRONTEND = frontend

venv:
	test -d $(VENV) || $(SYSTEM_PYTHON) -m venv $(VENV)
	test -d $(VENV_DATA_COLLECTOR) || $(SYSTEM_PYTHON) -m venv $(VENV_DATA_COLLECTOR)

install: venv
	. $(VENV)/bin/activate && $(PIP) install -r requirements.txt
	. $(VENV_DATA_COLLECTOR)/bin/activate && $(PIP_DATA_COLLECTOR) install -r $(DATA_COLLECTOR)/requirements.txt

install-dev: install
	. $(VENV)/bin/activate $(PIP) install -r requirements_dev.txt
	. $(VENV_DATA_COLLECTOR)/bin/activate && $(PIP_DATA_COLLECTOR) install -r $(DATA_COLLECTOR)/requirements_dev.txt

install-ui:
	npm install --prefix $(FRONTEND)

lint:
	. $(VENV)/bin/activate && $(VENV)/bin/pylint config.py wsgi.py application/
	. $(VENV_DATA_COLLECTOR)/bin/activate && $(VENV_DATA_COLLECTOR)/bin/pylint $(DATA_COLLECTOR)/data_collector.py

lint-ui:
	npm run --prefix $(FRONTEND) lint

flake8:
	. $(VENV)/bin/activate && $(VENV)/bin/flake8 config.py wsgi.py application/
	. $(VENV_DATA_COLLECTOR)/bin/activate && $(VENV_DATA_COLLECTOR)/bin/flake8 $(DATA_COLLECTOR)/data_collector.py

testing:
	. $(VENV)/bin/activate && pytest --cov=application tests/

testing-ui:
	npm run --prefix $(FRONTEND) test:unit

checking: lint flake8 testing lint-ui testing-ui

create-env:
ifeq ($(shell test -s .env && echo -n 0), 0)
	@echo 'Nothing to be done for create-env - .env file exists.'
else
	cp .env.example .env
	. $(VENV)/bin/activate && $(PYTHON) -c 'import os; print("SECRET_KEY={}".format(os.urandom(24)))' >> .env
endif

create-config:
ifeq ($(shell test -s data-usage-monitor.ini && echo -n 0), 0)
	@echo 'Nothing to be done for create-config - data-usage-monitor.ini file exists.'
else
	cp data-usage-monitor.ini.example data-usage-monitor.ini
endif

copy-config:
ifeq ($(shell test -s $(DATA_COLLECTOR)/data-usage-monitor.ini && echo -n 0), 0)
	@echo 'Nothing to be done for copy-config - data_collector/data-usage-monitor.ini file exists.'
else
	cp data-usage-monitor.ini $(DATA_COLLECTOR)/data-usage-monitor.ini
endif

prepare: install install-ui create-env create-config

upgrade-db:
	. $(VENV)/bin/activate && flask db upgrade

downgrade-db:
	. $(VENV)/bin/activate && flask db downgrade base

run-flask:
	. $(VENV)/bin/activate && $(PYTHON) wsgi.py

run-uwsgi:
	. $(VENV)/bin/activate && uwsgi --ini data-usage-monitor.ini

run-data-collector:
	. $(VENV_DATA_COLLECTOR)/bin/activate && $(PYTHON_DATA_COLLECTOR) $(DATA_COLLECTOR)/data_collector.py

run-ui:
	export VUE_APP_USE_MOCKED_VALUES=false && npm run --prefix $(FRONTEND) serve

run-ui-mock:
	export VUE_APP_USE_MOCKED_VALUES=true && npm run --prefix $(FRONTEND) serve

clean:
	rm -rf __pycache__
	rm -rf $(VENV)
	rm -rf $(DATA_COLLECTOR)/__pycache__
	rm -rf $(VENV_DATA_COLLECTOR)
	rm -rf $(FRONTEND)/node_modules
	
.PHONY: venv install install-dev install-ui lint lint-ui flake8 testing testing-ui checking create-env create-config copy-config prepare upgrade-db run-app run-data-collector run-ui run-ui-mock clean
