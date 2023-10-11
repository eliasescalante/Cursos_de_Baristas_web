from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    nacimiento = models.DateField()
    gustos = models.CharField(max_length=40)


    

class Tutor(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    edad = models.IntegerField()
    email = models.EmailField()

    

class Curso(models.Model):
    curso = models.CharField(max_length=40)
    tutor = models.CharField(max_length=40)
    cupo = models.IntegerField()
    fecha = models.DateField()
    
    