# Huawei data usage monitor

A simple data usage monitor for Huawei routers.
For now it only shows current usage - the value is updated by 1 minute.

## How to use it ?

### Clone this repository

`git clone https://github.com/kjuraszek/data-usage-monitor`

### Prepare a virtual environment

Create and activate a virtual environment (if not exists):

`make venv`

and then activate it:

`. venv/bin/activate`

### Install dependencies

`make install`

### Run app

Run a new terminal window, activate venv and run data-loader:

`make run-data-loader`

and finally run the app:

`make run-app`
