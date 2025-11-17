from datetime import datetime, timedelta

DATE_FORMATS = ("%Y-%m-%d", "%Y%m%d")

def aplicar_filtros(qs, request):
    data = request.GET.get("data")
    hoje = datetime.now().date()
    sete_dias_atras = hoje - timedelta(days=7)

    if data:
        data = _parse_date_str(data)

        if not (sete_dias_atras <= data <= hoje):
            raise ValueError("Parâmetro 'data' deve ser a data de hoje ou até 7 dias atrás.")

        qs = qs.filter(data_medicao__date=data)
        return qs

    return qs

def _parse_date_str(date_srt):
    for format in DATE_FORMATS:
        try:
            return datetime.strptime(date_srt, format).date()
        except ValueError:
            continue
    raise ValueError(f'Parâmetro de data fora do padrão. Formatos aceitos: {DATE_FORMATS}')
