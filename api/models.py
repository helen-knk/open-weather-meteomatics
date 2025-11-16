from django.db import models


class Clima(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    status_code = models.IntegerField()
    url = models.TextField(default='url')
    ok = models.TextField()
    response = models.JSONField()

    def __str__(self):
        return f'Clima - {self.data_criacao}'
