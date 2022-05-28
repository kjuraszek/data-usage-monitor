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
	$(PIP) install -r requirements_dev.txt

lint:
	. $(VENV)/bin/activate && $(VENV)/bin/pylint config.py data_loader.py wsgi.py application/

flake8:
	. $(VENV)/bin/activate && $(VENV)/bin/flake8 config.py data_loader.py wsgi.py application/

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

upgrade-db:
	. $(VENV)/bin/activate && flask db upgrade

downgrade-db:
	. $(VENV)/bin/activate && flask db downgrade base

run-app:
	. $(VENV)/bin/activate && flask run

run-data-loader:
	. $(VENV)/bin/activate && $(PYTHON) data_loader.py

clean:
	rm -rf __pycache__
	rm -rf $(VENV)
	
.PHONY: venv install install-dev lint flake8 create-env create-config upgrade-db run-app run-data-loader clean
