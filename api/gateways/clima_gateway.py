from api.models import Clima

def salvar_clima(dados):
    Clima.objects.create(
        status_code=dados.get('status_code'),
        ok=dados.get('ok'),
        url=dados.get('url'),
        response=dados.get('response')
    )
