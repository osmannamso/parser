from django.db import models

class Twogis(models.Model):
    oid = models.FloatField()
    address = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    lat = models.CharField(max_length=255)
    lon = models.CharField(max_length=255)