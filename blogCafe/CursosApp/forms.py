from django import forms
from .models import Comentario


#formulario curso
class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length = 40)
    tutor = forms.CharField(max_length = 40)
    cupo = forms.IntegerField()
    fecha = forms.DateField()
#    imagen = forms.ImageField()
#    descripcion = forms.CharField()

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
