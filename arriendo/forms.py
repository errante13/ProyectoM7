from django import forms
from django.contrib.auth.models import User
from .models import Usuario

class UserEditarForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = ['first_name','last_name']


class UsuarioForms(forms.ModelForm):
    class Meta: 
        model = Usuario
        fields = ['rut','direccion','telefono']