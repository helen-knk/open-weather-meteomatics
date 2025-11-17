from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

lista_clima_swwager = swagger_auto_schema(
    methods=['GET'],
    manual_parameters=[
        openapi.Parameter(
            name='data',
            in_=openapi.IN_QUERY,
            description=(
                "Filtrar por data no formato YYYYMMDD. "
                "Aceita apenas hoje ou datas de até 7 dias atrás."
            ),
            type=openapi.TYPE_STRING,
            required=False,
            example="20251117"
        ),
    ],
    responses={
        200: "Retorna dados climáticos de Joinville, agrupados por data",
        400: "Parâmetro inválido (data fora do intervalo permitido)"
    }
)
