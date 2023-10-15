from django.contrib import admin
from django.urls import path
from CursosApp import views


urlpatterns = [
    path('', views.inicio ,name="Inicio"),
    path('cursos_imprimir', views.imprimir_cursos ,name="Cursos"),
    path('estudiantes', views.estudiantes,name="Estudiantes"),
    path('nosotros', views.nosotros,name="Nosotros"),
    path('clases/detalle/<int:pk>', views.CursoDetalle.as_view(), name='Detalle'),
    path('filtrado/', views.filtrado, name='Filtrado'),
    path('arte/', views.arte, name='Arte'),
    path('barista/', views.barista, name='Barista'),
    path('expreso/', views.expreso, name='Expreso'),
    path('infusores/', views.infusores, name='Infusores'),
    path('tostado/', views.tostado, name='Tostado'),
]


