
from django.db import models

# Create your models here.

class Datos(models.Model):
    nombre = models.CharField(max_length=128)
    fecha_nacimiento = models.DateField()
    peso_kg = models.IntegerField()

    
    


class Interesante(models.Model):
    profesion = models.CharField(max_length=128)
    hobbys = models.CharField(max_length=128)
    proyecto_familia = models.ForeignKey('Datos', on_delete=models.CASCADE, null=True)


    