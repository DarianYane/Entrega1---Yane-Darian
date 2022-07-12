from django.db import models

# Creo la clase / el modelo de mis familiares
class Familiar(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    email = models.EmailField(max_length=100)
    fecha_nacimiento = models.DateField() #(YYYY-MM-DD)

class Electrodomestico(models.Model):
    tipoE = models.CharField(max_length=40)
    marcaE = models.CharField(max_length=40)
    modeloE = models.CharField(max_length=40)
    precio = models.IntegerField()
    #email = models.EmailField(max_length=100)
    fecha_produccionE = models.DateField() #(YYYY-MM-DD)

class Vehiculo(models.Model):
    tipoV = models.CharField(max_length=40)
    marcaV = models.CharField(max_length=40)
    modeloV = models.CharField(max_length=40)
    ruedas = models.IntegerField()
    #email = models.EmailField(max_length=100)
    fecha_produccionV = models.DateField() #(YYYY-MM-DD)