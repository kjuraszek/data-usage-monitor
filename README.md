# Huawei data usage monitor

A simple data usage monitor for Huawei routers.
For now it only shows current usage - the value is updated by 1 minute.

## How to use it ?

### Prerequisites

- Unix OS
- GNU Make
- and either :
  - Python 3.9
  - node with npm
  - PostgreSQL database
- or :
  - Docker and Docker-compose

### Clone this repository

`git clone https://github.com/kjuraszek/data-usage-monitor`

### Prepare .env and .ini files

This step:

- creates an .env file
- creates an data-usage-monitor.ini files
- prepares a virtual environments and install dependencies (if not using Docker)

If you prefer to use Docker run the command `make prepare-env` and move to [Update database connection details](#update-database-connection-details) section.

Otherwise - run the command `make prepare` and move to [Update database connection details](#update-database-connection-details) section.

Or if you prefer to run each step separately follow below steps.

#### Prepare a virtual environment

Create virtual environments (if they don't exist):

`make venv`

#### Install dependencies

`make install` command installs dependencies for backend and data_collector
`make install-ui` command installs dependencies for frontend

#### Create .env

This command creates an .env file (which contains environment variables) and generates a SECRET_KEY for a Flask app.

`make create-env`

#### Create data-usage-monitor.ini file

This command creates an .ini config file (which contains configuration options).

`make create-config`

### Update database connection details

This project uses PostgreSQL database - after creating `.env` file edit variables starting of `POSTGRES_` and change their values to proper values of your database credentials:

- `<DB_USER>` - database user name
- `<DB_PASSWORD>` - database user password
- `<DB_HOST>` - database host
- `<DB_PORT>` - database port
- `<DB_NAME>` - database name

Examplary values:

    POSTGRES_HOST=localhost
    POSTGRES_PORT=5432
    POSTGRES_DATABASE=data-monitor
    POSTGRES_USER=data-monitor
    POSTGRES_PASSWORD=my$ECR#Tpwd

### Running app in Docker containers

*if you prefer to run app from the command line move to* [Run app from the command line](#run-app-from-the-command-line) *section*.

Build images with command :

- `make build-docker` or
- `make build-docker-mock` - to build frontend image with mocked data

To start containers run `make run-docker` command.
Application should be by default accessible on :

- [localhost:8080/](http://localhost:8080/) for frontend
- [localhost:5000/](http://localhost:5000/) for backend

To stop containers run `make stop-docker` command.

### Run app from the command line

Set up the database:

`make upgrade-db`

Run data-collector:

`make run-data-collector`

Open a new terminal window and run:

- `make run-flask` for development server or
- `make run-uwsgi` for production server.

Open a new terminal window and run:

- `make run-ui-mock` to run UI with a mocked data or
- `make run-ui` to run UI with the data from an API

Application should be by default accessible on:

- [localhost:8080/](http://localhost:8080/) for frontend
- [localhost:5000/](http://localhost:5000/) for backend

### Cleaning the data and database

To clean created data run:

- `make reset-db` - this command cleans database
- `make clean` - this command removes created .ini config files, .env file, virtual environments and node_modules
- `make clean-docker` - this command removes created Docker images, containers and volumes

### \[Optional\] Running tests

This applies only for non-Docker set up.

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
