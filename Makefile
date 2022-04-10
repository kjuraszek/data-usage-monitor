VENV = venv
PYTHON_VERSION = 3.9
SYSTEM_PYTHON = $(shell which python$(PYTHON_VERSION))
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

venv:
	test -d $(VENV) || $(SYSTEM_PYTHON) -m venv $(VENV)

install: venv
	. $(VENV)/bin/activate && $(PIP) install -r requirements.txt

run-app:
	. $(VENV)/bin/activate && flask run

run-data-loader:
	. $(VENV)/bin/activate && $(PYTHON) data-loader.py

clean:
	rm -rf __pycache__
	rm -rf $(VENV)
	
.PHONY: venv install run-app run-data-loader clean
