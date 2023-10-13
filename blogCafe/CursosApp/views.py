from django.shortcuts import render
from django.views.generic import  DetailView
from .models import *
# Create your views here.

################################################################ 

def inicio(request):
    #pagina de inicio
    return render(request, 'CursosApp/index.html')

def cursos(request):
    return render(request, 'CursosApp/cursos.html')

def estudiantes(request):
    return render(request, 'CursosApp/estudiantes.html')

def nosotros(request):
    return render ( request , "CursosApp/nosotros.html" )

###################################################################

def imprimir_cursos(request):

    cursos = Curso.objects.all()
    
    context = {
        'cursos': cursos
    }
    return render(request, r"CursosApp\cursos.html",context)

class CursoDetalle(DetailView):
    
    model=Curso
    template_name='CursosApp/curso_detalle.html'



