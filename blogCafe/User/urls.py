from django.urls import path
from .views import UsuarioEdicion, CambioPassword
from User import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    # path('edicionPerfil', UsuarioEdicion.as_view(), name = 'editar_perfil'),
    path('edicionPerfil', views.edit, name = 'editar_perfil'),
    path('cambio_exitoso/',views.cambio_exitoso, name="Edicion_ok"),
    path('contra_exitosa/', views.contra_exitosa, name = "Contrasenia_exitosa" ),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('logout', LogoutView.as_view(template_name='CursosApp/index.html'), name="Logout"),
]
