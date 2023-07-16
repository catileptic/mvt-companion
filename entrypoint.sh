#!/bin/sh

python manage.py migrate --no-input

DJANGO_SUPERUSER_PASSWORD=$SUPER_USER_PASSWORD python manage.py createsuperuser --username $SUPER_USER_NAME --email $SUPER_USER_EMAIL --noinput

python manage.py runserver 0.0.0.0:8000
