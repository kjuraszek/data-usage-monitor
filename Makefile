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
	. $(VENV)/bin/activate && $(VENV)/bin/pylint config.py data-loader.py wsgi.py application/

flake8:
	. $(VENV)/bin/activate && $(VENV)/bin/flake8 config.py data-loader.py wsgi.py application/

run-app:
	. $(VENV)/bin/activate && flask run

run-data-loader:
	. $(VENV)/bin/activate && $(PYTHON) data-loader.py

clean:
	rm -rf __pycache__
	rm -rf $(VENV)
	
.PHONY: venv install install-dev lint flake8 run-app run-data-loader clean
