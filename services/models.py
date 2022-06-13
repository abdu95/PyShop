from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    status = models.CharField(max_length=255)
    image_url = models.CharField(max_length=2083)
