from django.conf import settings
from django.http import HttpResponseForbidden


class BlockNonLocalMiddleware:
    """
    Bloqueia acesso à raiz '/' e ao '/admin/' se não for ambiente local.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not settings.DEBUG:
            if request.path in ['/', '/admin/']:
                return HttpResponseForbidden('Acesso negado fora do ambiente local.')
        return self.get_response(request)
