VENV = venv
PYTHON_VERSION = 3.9
SYSTEM_PYTHON = $(shell which python$(PYTHON_VERSION))
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

venv:
	test -d $(VENV) || $(SYSTEM_PYTHON) -m venv $(VENV)

install: venv
	. $(VENV)/bin/activate && $(PIP) install -r requirements.txt

install-dev: install
	. $(VENV)/bin/activate $(PIP) install -r requirements_dev.txt

install-ui:
	npm install --prefix frontend

lint:
	. $(VENV)/bin/activate && $(VENV)/bin/pylint config.py data_collector.py wsgi.py application/

lint-ui:
	npm run --prefix frontend lint

flake8:
	. $(VENV)/bin/activate && $(VENV)/bin/flake8 config.py data_collector.py wsgi.py application/

testing:
	. $(VENV)/bin/activate && pytest --cov=application tests/

testing-ui:
	npm run --prefix frontend test:unit

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
	. $(VENV)/bin/activate && $(PYTHON) data_collector.py

run-ui:
	export VUE_APP_USE_MOCKED_VALUES=false && npm run --prefix frontend serve

run-ui-mock:
	export VUE_APP_USE_MOCKED_VALUES=true && npm run --prefix frontend serve

clean:
	rm -rf __pycache__
	rm -rf $(VENV)
	
.PHONY: venv install install-dev install-ui lint lint-ui flake8 testing testing-ui checking create-env create-config prepare upgrade-db run-app run-data-collector run-ui run-ui-mock clean
