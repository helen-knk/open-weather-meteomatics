from celery import shared_task
from api.services.clima_service import consultar_clima


@shared_task
def consultar_clima_task():
    return consultar_clima()
