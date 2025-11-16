#!/bin/sh
echo "🟩 Iniciando ambiente de Produção..."

python manage.py migrate
python manage.py collectstatic --noinput

echo "Iniciando Gunicorn..."
gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers 3 --timeout 120
