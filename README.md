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

`make install`

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

### set up the database

`make upgrade-db`

### Run app

Run data-collector:

`make run-data-collector`

Open a new terminal window, activate venv and run:

- `make run-flask` for development server or
- `make run-uwsgi` for production server.
