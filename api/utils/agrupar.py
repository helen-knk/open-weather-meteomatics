from api.utils.clima_stats import calcular_media_temperatura, calcular_minima_temperatura, calcular_maxima_temperatura


def agrupar_por_dia(queryset):
    resultado = {}

    for item in queryset:
        data = item['data_medicao'].date().isoformat()
        if data not in resultado:
            resultado[data] = []

        resultado[data].append({
            'data_medicao': item['data_medicao'].replace(microsecond=0),
            'temperatura': item['temperatura'],
            'precipitacao': item['precipitacao'],
            'vento': item['vento'],
        })

    saida = []
    for data, valores in resultado.items():
        saida.append({
            'data': data,
            'media_temperatura': calcular_media_temperatura(valores),
            'minima_temperatura': calcular_minima_temperatura(valores),
            'maxima_temperatura': calcular_maxima_temperatura(valores),
            'valores': valores
        })

    return saida
