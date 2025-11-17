from datetime import datetime
from http import HTTPStatus

from api.models import Clima, ClimaDados

PARAMETRO_MAP = {
    't_2m:C': 'temperatura',
    'precip_1h:mm': 'precipitacao',
    'wind_speed_10m:ms': 'vento'
}


def salvar_clima(dados):
    log = salvar_log(dados)
    processar_dados_clima(log)

def obter_clima():
    return Clima.objects.order_by('-data_criacao').values()

def salvar_log(dados):
    log = Clima.objects.create(
        status_code=dados.get('status_code'),
        ok=dados.get('ok'),
        url=dados.get('url'),
        response=dados.get('response')
    )
    return log

def processar_dados_clima(log):
    if log.status_code != HTTPStatus.OK:
        return

    dados_json = log.response
    agrupar = {}

    for item in dados_json.get('data', []):
        parametro = item.get('parameter')
        campo = PARAMETRO_MAP.get(parametro)
        if not campo:
            continue

        for coord in item.get('coordinates', []):
            for d in coord.get('dates', []):
                data_medicao = d.get('date')
                valor = d.get('value')

                if data_medicao not in agrupar:
                    agrupar[data_medicao] = {
                        'temperatura': None,
                        'precipitacao': None,
                        'vento': None
                    }

                agrupar[data_medicao][campo] = valor

    for data_iso, valores in agrupar.items():
        data_dt = datetime.strptime(data_iso, "%Y-%m-%dT%H:%M:%SZ")
        ClimaDados.objects.create(
            clima=log,
            data_medicao=data_dt,
            **valores
        )
