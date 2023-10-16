from django.shortcuts import render , redirect
from django.views.generic import  DetailView,CreateView, UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import FormularioComentario
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
        mi_formulario = FormularioComentario(request.POST)

        if mi_formulario.is_valid():
                data = mi_formulario.cleaned_data
                curso = Curso.objects.get(pk=curso_id)  # Obtén el objeto Curso correspondiente
                comentarios = Comentario(nombre=data['nombre'], mensaje=data['mensaje'], comentario=curso)
                comentarios.save()
                return redirect('CursosApp/curso_detalle', curso_id=curso_id)  # Redirigir a la página de éxito

            
    else:
        # Si no se envió el formulario, mostrar el formulario en blanco
        mi_formulario = FormularioComentario()

    return render(request, 'CursosApp/comentario.html', {'mi_formulario': mi_formulario, 'curso_id': curso_id})     



