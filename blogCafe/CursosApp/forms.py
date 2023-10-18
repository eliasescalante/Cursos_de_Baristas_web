from django import forms
from .models import Comentario, Alumno


#formulario curso
class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length = 40)
    tutor = forms.CharField(max_length = 40)
    cupo = forms.IntegerField()
    fecha = forms.DateField()
    imagen = forms.ImageField()
    descripcion = forms.CharField()

    def _str__(self):
        return self.nombre


class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje' : forms.Textarea(attrs={'class': 'form-control'}),
        }


class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'email', 'nacimiento', 'gustos']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gustos': forms.TextInput(attrs={'class': 'form-control'}),
          }
