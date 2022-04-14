#!/bin/sh

set -e

python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
# DJANGO_SUPERUSER_PASSWORD=superuser python manage.py createsuperuser --noinput --username=admin  --email=anaya.garay98@gmail.com


gunicorn backend.wsgi:application --bind 0.0.0.0:8000


