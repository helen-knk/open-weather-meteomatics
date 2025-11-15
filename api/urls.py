from django.urls import path

from .views import listar_dados_climaticos_cidade

urlpatterns = [
    path('clima/', listar_dados_climaticos_cidade),
]
