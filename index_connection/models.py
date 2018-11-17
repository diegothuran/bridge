from django.db import models


class Relevancia_site(models.Model):
    site = models.TextField()
    relevancia = models.FloatField()
    relevancia_inicial = models.FloatField()
