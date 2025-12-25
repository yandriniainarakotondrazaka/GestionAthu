from django.db import models

class Utilisateur(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Voiture(models.Model):
    marque = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    nombre = models.IntegerField()
def __str__(self):
    return self.marque