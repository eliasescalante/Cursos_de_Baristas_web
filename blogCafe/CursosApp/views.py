from django.shortcuts import render
from django.views.generic import  DetailView,CreateView, UpdateView
from django.urls import reverse_lazy
from .models import *
# Create your views here.

################################################################ 

def inicio(request):
    #pagina de inicio
    return render(request, 'CursosApp/index.html')

def cursos(request): 
    #pagina de curso
    return render(request, 'CursosApp/cursos.html')

def estudiantes(request):
    #pagina de estudiantes
    return render(request, 'CursosApp/estudiantes.html')

def nosotros(request):
    #pagina sobre nosotros
    return render ( request , "CursosApp/nosotros.html" )

###################################################################

def imprimir_cursos(request):
    #pagina para imprimir los cursos
    cursos = Curso.objects.all()

    context = {
        'cursos': cursos
    }
    return render(request, r"CursosApp\cursos.html",context)

class CursoDetalle(DetailView):
    #pagina para los detalles de los cursos
    model = Curso
    template_name = 'CursosApp/curso_detalle.html'

class CursoCreateView(CreateView):
      model = Curso
      template_name = "CursosApp/cursoFormulario.html"
      success_url = reverse_lazy("Nuevo")
      fields= ["nombre","tutor","cupo","fecha","descripcion"]

class CursoUpdateView(UpdateView):
      model = Curso
      template_name = "CursosApp/cursoEdit.html"
      success_url = reverse_lazy("Editar")
      fields= ["nombre","tutor"]


############################################
def crear_comentario(request, curso_id):
    if request.method == 'POST':
        # Si se envió el formulario, procesar los datos enviados
        formulario = FormularioComentario(request.POST)

        if formulario.is_valid():
            # Si el formulario es válido, guardar el comentario en la base de datos
            formulario.save()
            return render('curso_detalle.html')  # Redirigir a la página de éxito
    else:
        # Si no se envió el formulario, mostrar el formulario en blanco
        formulario = FormularioComentario()

    return render(request, 'CursosApp/comentario.html', {'formulario': formulario})     



