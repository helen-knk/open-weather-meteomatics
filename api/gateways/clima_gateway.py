from api.models import Clima

def salvar_clima(dados):
    Clima.objects.create(
        status_code=dados.get('status_code'),
        ok=dados.get('ok'),
        url=dados.get('url'),
        response=dados.get('response')
    )

def obter_clima():
    return Clima.objects.order_by('-data_criacao').values()