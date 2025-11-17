from http import HTTPStatus

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.documentation.clima_endpoints import lista_clima_swwager
from api.filters import aplicar_filtros
from api.services.clima_service import listar_clima
from api.utils.agrupar import agrupar_por_dia

@lista_clima_swwager
@api_view(['GET'])
def listar_registros_clima(request):
    try:
        qs = listar_clima()
        qs = aplicar_filtros(qs, request)
        dados = agrupar_por_dia(qs)
        return Response(dados)

    except ValueError as e:
        return Response({'erro': str(e)}, status=HTTPStatus.BAD_REQUEST)
