from django.db import models

class Paleta(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    descripcion = models.TextField()
    
