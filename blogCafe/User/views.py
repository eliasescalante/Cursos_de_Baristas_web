from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from User.forms import  UserRegisterForm



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

