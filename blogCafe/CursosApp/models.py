from django.db import models
from django.utils import timezone

# Create your models here.


#modelo alumno

class Alumno(models.Model):
    usuario = models.CharField(max_length=40, null=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    nacimiento = models.DateField(null=True)
    gustos = models.CharField(max_length=40)
    cursos_inscriptos = models.ManyToManyField('Curso', blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

#modelo de curso
class Curso(models.Model):


    nombre = models.CharField(max_length=40)
    tutor = models.CharField(max_length=40)
    cupo = models.IntegerField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to="cursos",null=True)
    descripcion = models.CharField(max_length=400, null = True)

    def _str__(self):
        return self.nombre


#modelo de comentario
class Comentario(models.Model):
    comentario = models.ForeignKey(Curso, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)