from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Clima API',
        default_version='v1',
        description='API para consultar dados climáticos salvos',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
