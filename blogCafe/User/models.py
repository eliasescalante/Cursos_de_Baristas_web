from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Clase 24
class Imagen(models.Model):
    #modelo de imagen para el avatar
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank = True)

    def __str__(self):
        return f"{settings.MEDIA_URL}{self.imagen}"

class Usuarios(User):
    cursos_inscriptos = models.TextField()

    def _str__(self):
        return self.cursos_inscriptos