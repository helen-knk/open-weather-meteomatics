from django.urls import path

from .views import listar_registros_clima

urlpatterns = [
    path('clima/', listar_registros_clima),
]
