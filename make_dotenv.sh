#!/bin/bash

SCRIPT_PATH="$(realpath "${BASH_SOURCE[-1]}")"
SCRIPT_DIRECTORY="$(dirname "$SCRIPT_PATH")"
ENV_FILE="${SCRIPT_DIRECTORY}/.env"

if ! test -f "$ENV_FILE"; then
    echo 'DEBUG=True' >> $ENV_FILE
    echo 'POSTGRES_DB=postgres' >> $ENV_FILE
    echo 'POSTGRES_USER=postgres' >> $ENV_FILE
    echo "POSTGRES_PASSWORD=$(tr -dc 'A-Za-z0-9' < /dev/urandom | head -c 16)" >> $ENV_FILE
    echo "SECRET_KEY=$(tr -dc 'A-Za-z0-9' < /dev/urandom | head -c 16)" >> $ENV_FILE
    echo "SUPER_USER_NAME=admin" >> $ENV_FILE
    echo "SUPER_USER_PASSWORD=$(tr -dc 'A-Za-z0-9' < /dev/urandom | head -c 16)" >> $ENV_FILE
    echo "SUPER_USER_EMAIL=root@localhost" >> $ENV_FILE
fi
