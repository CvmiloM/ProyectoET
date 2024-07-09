# miapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UsuarioAdmin, Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 'imagen', 'stock'] 
class UsuarioAdminForm(UserCreationForm):
    class Meta:
        model = UsuarioAdmin
        fields = ['username', 'password1', 'password2']


from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class FormUsuario(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']