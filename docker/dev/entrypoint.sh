#!/bin/bash

echo "🟦 Ambiente de Desenvolvimento iniciado"
python manage.py migrate

python manage.py runserver 0.0.0.0:8000
