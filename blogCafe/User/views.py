from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from User.forms import UserEditForm, UserRegisterForm
from User.models import Imagen


# Create your views here.
def login_request(request):

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
    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Si los datos ingresados en el form son válidos, con form.save()
            # creamos un nuevo user usando esos datos
            form.save()
            return render(request,"CursosApp/index.html")
        
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()     
    return render(request,"User/registro.html" ,  {"form":form, "msg_register": msg_register})

# Vista de editar el perfil
@login_required
def edit(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            if informacion["password1"] != informacion["password2"]:
                datos = {
                    'first_name': usuario.first_name,
                    'email': usuario.email
                }
                miFormulario = UserEditForm(initial=datos)

            else:
                usuario.email = informacion['email']
                if informacion["password1"]:
                    usuario.set_password(informacion["password1"])
                usuario.last_name = informacion['last_name']
                usuario.first_name = informacion['first_name']
                usuario.save()

                # Creamos nueva imagen en la tabla
                try:
                    avatar = Imagen.objects.get(user=usuario)
                except Imagen.DoesNotExist:
                    avatar = Imagen(user=usuario, imagen=informacion["imagen"])
                    avatar.save()
                else:
                    avatar.imagen = informacion["imagen"]
                    avatar.save()

                return render(request, "CursosApp/index.html")

    else:
        datos = {
            'first_name': usuario.first_name,
            'email': usuario.email
        }
        miFormulario = UserEditForm(initial=datos)

    return render(request, "User/edit.html", {"mi_form": miFormulario, "usuario": usuario})