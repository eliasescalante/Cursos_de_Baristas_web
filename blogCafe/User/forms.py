from django import forms
from django.contrib.auth.forms import UserCreationForm, User, PasswordChangeForm


class UserEditForm(UserCreationForm):

    password = None
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        help_text = {k: "" for k in fields}

class CambioDeContrasenia(PasswordChangeForm):
    contrasenia_vieja = forms.CharField(label=("Contraseña Actual"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_contrasenia1 = forms.CharField(label=("Nueva Contraseña"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_contrasenia2 = forms.CharField(label=("Repita Nueva Contraseña"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('contrasenia_vieja', 'new_contrasenia1', 'new_contrasenia2')