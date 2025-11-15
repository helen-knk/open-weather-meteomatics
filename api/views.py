from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.services.external_api import request_get

@api_view(['GET'])
def listar_dados_climaticos_cidade(request):
    dados  = request_get()
    return Response(dados)
