from django import forms
from django.contrib.auth.forms import UserCreationForm, User, PasswordChangeForm

# formulario para editar el usuario

class UserEditForm(UserCreationForm):

    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput, required=False)

    last_name = forms.CharField(required=False)
    first_name = forms.CharField(required=False)
    imagen = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name', 'password1', 'password2']



#formulario para registrar usuario
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        help_text = {k: "" for k in fields}
#formulario para cambiar contraseña


class CambioDeContrasenia(PasswordChangeForm):
    contrasenia_vieja = forms.CharField(label=("Contraseña Actual"), widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_contrasenia1 = forms.CharField(label=("Nueva Contraseña"), widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_contrasenia2 = forms.CharField(label=("Repita Nueva Contraseña"),widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('contrasenia_vieja', 'new_contrasenia1', 'new_contrasenia2')