#!/bin/bash

DJANGO_SETTINGS_MODULE=Bostan.settings.prod

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn Bostan.wsgi:application \
    --bind 0.0.0.0:80 \
    --workers 3