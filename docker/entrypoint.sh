#!/bin/bash

echo "Aguardando o MySQL..."
while ! python -c "import pymysql; pymysql.connect(host='$DB_HOST', user='$DB_USER', password='$DB_PASSWORD')" 2>/dev/null; do
    sleep 5
done

echo "MySQL pronto! Rodando migrations..."
python manage.py migrate

exec "$@"
