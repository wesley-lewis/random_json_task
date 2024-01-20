from django.db import models

class Data(models.Model):
    def __str__(self):
        return self.email
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=15)

class DynData(models.Model):
    randomdata = models.JSONField()
