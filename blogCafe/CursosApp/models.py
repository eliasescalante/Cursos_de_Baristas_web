from django.db import models

# Create your models here.

class Alumno(models.Model):

    # modelo de alumno

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    nacimiento = models.DateField()
    gustos = models.CharField(max_length=40)


class Curso(models.Model):

    #modelo de curso

    nombre = models.CharField(max_length=40)
    tutor = models.CharField(max_length=40)
    cupo = models.IntegerField()
    fecha = models.DateField()
    
    