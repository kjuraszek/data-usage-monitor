# Huawei data usage monitor

A simple data usage monitor for Huawei routers.
For now it only shows current usage - the value is updated by 1 minute.

## How to use it ?

### Clone this repository

`git clone https://github.com/kjuraszek/data-usage-monitor`

### Prepare an environment

This step:

- prepares a virtual environment and install dependencies
- creates an .env file
- creates an data-usage-monitor.ini file

Run the command:

`make prepare`

and then activate a virtual environment:

`. venv/bin/activate`

If you prefer to run each step separately follow below steps. Otherwise move to [Update database connection details](#update-database-connection-details) section.

#### Prepare a virtual environment

Create and activate a virtual environment (if not exists):

`make venv`

and then activate it:

`. venv/bin/activate`

#### Install dependencies

`make install` command installs dependencies for backend
`make install-ui` command installs dependencies for frontend

#### Create .env

This command creates an .env file (which contains environment variables) and generates a SECRET_KEY for a Flask app.

`make create-env`

#### Create data-usage-monitor.ini file

This command creates an .ini config file (which contains configuration options).

`make create-config`

### Update database connection details

After creating `.env` file edit value of `SQLALCHEMY_DATABASE_URI` and change values to proper values of your database credentials:

- `<DB_USER>` - database user name
- `<DB_PASSWORD>` - database user password
- `<DB_HOST>` - database host
- `<DB_PORT>` - database port
- `<DB_NAME>` - database name

This project uses PostgreSQL database - if you prefer to use other DB engine also change value of postgresql in `SQLALCHEMY_DATABASE_URI` and a proper database driver in the requirements.txt file.

### Set up the database

`make upgrade-db`

### Run app

Run data-collector:

`make run-data-collector`

Open a new terminal window, activate venv and run:

- `make run-flask` for development server or
- `make run-uwsgi` for production server.

Open a new terminal window, activate venv and run:

- `make run-ui-mock` to run UI with a mocked data or
- `make run-ui` to run UI with the data from an API

### Cleaning the data and database

To clean created data run:

- `make reset-db` - this command cleans database
- `make clean` - this command removes created .ini config files, .env file, virtual environments and node_modules

### \[Optional\] Running tests

#### Install dev dependencies

Before running tests and linting use `make install-dev` after installing core dependecies

#### Check all

To run linting and tests simply run `make checking`

#### Check linting

To check linting:

- `make lint` and `make flake8` for backend and
- `make lint-ui` for UI

#### Run tests

To run tests:

- `make testing` for backend and
- `make testing-ui` for UI
