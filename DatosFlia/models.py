from django.db import models

# Creo la clase / el modelo de mis familiares
class Familiar(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    email = models.EmailField(max_length=100)
    fecha_nacimiento = models.DateField() #(YYYY-MM-DD)