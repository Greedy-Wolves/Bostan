#!/bin/bash

DJANGO_SETTINGS_MODULE=Bostan.settings.prod

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn Bostan.wsgi:application \
    --bind 0.0.0.0:80 \
    --workers 3