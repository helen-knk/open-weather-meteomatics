
def calcular_media_temperatura(valores):
    temps = lista_temperaturas(valores)
    return round(sum(temps) / len(temps), 2) if temps else None

def calcular_minima_temperatura(valores):
    temps = lista_temperaturas(valores)
    return min(temps) if temps else None

def calcular_maxima_temperatura(valores):
    temps = lista_temperaturas(valores)
    return max(temps) if temps else None
    
def lista_temperaturas(valores):
    return [v["temperatura"] for v in valores if v["temperatura"] is not None]