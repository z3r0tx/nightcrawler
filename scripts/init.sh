#!/bin/bash
set -e

export PGUSER=$(grep DB_USER .env | cut -d '=' -f 2-)
export PGPASSWORD=$(grep DB_PASSWORD .env | cut -d '=' -f 2-)
export PGDATABASE=$(grep DB_NAME .env | cut -d '=' -f 2-)
export PGHOST=$(grep DB_HOST .env | cut -d '=' -f 2-)

psql -h $PGHOST -U $PGUSER -d $PGDATABASE -f init.sql
