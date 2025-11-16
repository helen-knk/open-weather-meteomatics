import requests
from decouple import config
import datetime

def buscar_dados_climaticos_da_api(
        latitude=-26.3044898,
        longitude=-48.8486726,
        data=None,
        parametros=None
):
    """
        Retorna dados climáticos da Meteomatics API.

        Por padrão, retorna dados de Joinville (latitude=-26.3044898, longitude=-48.8486726).
        Pode passar outras coordenadas se necessário.
    """
    login = config('USER_METEOMATICS_API')
    senha = config('PASSWORD_METEOMATICS_API')

    if data is None:
        data = datetime.date.today()
    start = f'{data}T00:00:00.000-03:00'
    end = f'{data}T23:59:59.000-03:00'
    data_range = f'{start}--{end}/'

    if parametros is None:
        parametros = ['t_2m:C', 'precip_1h:mm', 'wind_speed_10m:ms']
    parametros_str = ','.join(parametros) + '/'

    coordenadas = f'{latitude},{longitude}/'

    tipo = 'json'

    url = f'https://api.meteomatics.com/{data_range}{parametros_str}{coordenadas}{tipo}'

    try:
        response = requests.get(url, auth=(login, senha))
        try:
            data = response.json()
        except ValueError:
            data = response.text

        return {
            "status_code": response.status_code,
            "ok": response.ok,
            "url": response.url,
            "response": data
        }

    except requests.RequestException as e:
        return {
            "status_code": None,
            "ok": False,
            "error": str(e),
            "url": url,
        }
