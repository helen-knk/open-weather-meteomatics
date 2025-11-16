import requests
from decouple import config

def buscar_dados_climaticos_da_api():
    login = config('USER_METEOMATICS_API')
    senha = config('PASSWORD_METEOMATICS_API')
    url = 'https://api.meteomatics.com/2025-11-14T21:45:00.000-03:00--2025-11-15T21:45:00.000-03:00/t_2m:C,precip_1h:mm,wind_speed_10m:ms/-26.3044898,-48.8486726/json'

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
