from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.services.clima_service import listar_clima


@api_view(['GET'])
def listar_registros_clima(request):
    registros = listar_clima()
    return Response(list(registros))
