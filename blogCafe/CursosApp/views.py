from django.shortcuts import render
from django.views.generic import  DetailView
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

    cursos = Curso.objects.all()

    context = {
        'cursos': cursos
    }
    return render(request, r"CursosApp\cursos.html",context)

class CursoDetalle(DetailView):

    model=Curso
    template_name='CursosApp/curso_detalle.html'


#VISTAS PARA LOS CURSOS DE CAFE
def filtrado(request):
    return render(request,'CursosApp/cursoFiltrado.html')

def arte(request):
    return render(request,'CursosApp/cursoArte.html')

def barista(request):
    return render(request,'CursosApp/cursoBaristaArte.html')

def expreso(request):
    return render(request,'CursosApp/cursoExpreso.html')

def infusores(request):
    return render(request,'CursosApp/cursoInfusores.html')

def tostado(request):
    return render(request,'CursosApp/cursoTostado.html')





