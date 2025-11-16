from api.clients.meteomatics_client import buscar_dados_climaticos_da_api
from api.gateways.clima_gateway import salvar_clima

def consultar_clima():
    api_resposta = buscar_dados_climaticos_da_api()
    salvar_clima(api_resposta)
