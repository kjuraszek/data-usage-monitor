#!/bin/bash
set -o allexport; . backend/.env; set +o allexport
export POSTGRES_HOST=db
export FLASK_ENV=production
python3 -m flask db upgrade --directory backend/migrations
uwsgi --ini backend/data-usage-monitor.ini