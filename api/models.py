from django.db import models


class Clima(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    status_code = models.IntegerField()
    url = models.TextField(default='url')
    ok = models.TextField()
    response = models.JSONField()

    def __str__(self):
        return f'Clima - {self.data_criacao}'

class ClimaDados(models.Model):
    clima = models.ForeignKey('Clima', on_delete=models.CASCADE, related_name='dados')
    data_medicao = models.DateTimeField()
    temperatura = models.FloatField(null=True, blank=True)
    precipitacao = models.FloatField(null=True, blank=True)
    vento = models.FloatField(null=True, blank=True)
