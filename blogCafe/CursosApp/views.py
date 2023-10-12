from django.shortcuts import render

# Create your views here.

def inicio(request):
    #pagina de inicio
    return render(request, 'CursosApp/index.html')

def cursos(request):
    return render(request, 'CursosApp/cursos.html')

def estudiantes(request):
    return render(request, 'CursosApp/estudiantes.html')

def nosotros(request):
    return render ( request , "CursosApp/nosotros.html" )