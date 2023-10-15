from django.shortcuts import render
from django.views.generic import UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import  PasswordChangeView
from User.forms import  UserRegisterForm
from django.urls import reverse_lazy
from User.forms import UserEditForm, CambioDeContrasenia

#esta funcionando esto 

# Create your views here.
def login_request(request):
    #formulario para el login
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            con = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=con)

            if user is not None:
                login(request,user)

                return render(request,"CursosApp/index.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request,"CursosApp/index.html",{"mensaje":"Error, datos incorrectos"})
        else:
            return render(request, "CursosApp/index.html", {"mensaje":"Error, formulario erroneo"})

    form = AuthenticationForm()
    return render (request,"User/login.html", {'form':form})
    

# Vista de registro
def register(request):

    if request.method == 'POST':

        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"CursosApp/index.html", {"mensaje":"Usuario creado..."})
    else:
        # form = UserCreationForm()
        form = UserRegisterForm()
    
    return render(request, "User/registro.html", {"form":form})

#vista del cambio ok
def cambio_exitoso(request):
    return render(request, 'User/cambio_exitoso.html')


#Vista de edicion de usuario
class UsuarioEdicion(UpdateView):
    form_class = UserEditForm
    template_name= 'User/perfil.html'
    success_url = reverse_lazy('Edicion_ok')

    def get_object(self):
        return self.request.user

#clase para cambiar el pass
class CambioPassword(PasswordChangeView):
    form_class = CambioDeContrasenia
    template_name = 'User/cambioPass.html'
    success_url = reverse_lazy('Contrasenia_exitosa')

# vista del cambio de pass exitoso    
def contra_exitosa(request):
    return render(request, 'User/contraseniaok.html', {})
