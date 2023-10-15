from django.db import models

# Create your models here.

class Alumno(models.Model):

    # modelo de alumno

    usuario = models.CharField(max_length=40,null=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    nacimiento = models.DateField()
    gustos = models.CharField(max_length=40)
    curso_inscripto = models.CharField(max_length=200, null = True)


class Curso(models.Model):

    #modelo de curso

    nombre = models.CharField(max_length=40)
    tutor = models.CharField(max_length=40)
    cupo = models.IntegerField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to="cursos",null=True)
    descripcion = models.CharField(max_length=400, null = True)

    def _str__(self):
        return self.nombre

class Comentario(models.Model):
    #modelo de comentarios

    nombre = models.CharField(max_length=20)
    comentario = models.CharField(max_length=200)