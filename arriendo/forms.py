from django import forms
from django.contrib.auth.models import User
from .models import Usuario,Inmueble

class UserEditarForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = ['first_name','last_name']


class UsuarioForms(forms.ModelForm):
    class Meta: 
        model = Usuario
        fields = ['rut','direccion','telefono']
        
class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['nombres', 'descripcion', 'm2_construidos', 'm2_terreno', 'nun_estacionamientos','num_habitaciones', 'num_banos', 'direccion', 'precio_mensual','region', 'comuna','tipo_inmueble']
        #'nun_estacionamientos'
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'm2_construidos': forms.NumberInput(attrs={'class': 'form-control'}),
            'm2_terreno': forms.NumberInput(attrs={'class': 'form-control'}),
            'nun_estacionamientos': forms.NumberInput(attrs={'class': 'form-control'}),
            'num_habitaciones': forms.NumberInput(attrs={'class': 'form-control'}),
            'num_banos': forms.NumberInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_mensual': forms.NumberInput(attrs={'class': 'form-control'}),
            'comuna': forms.Select(attrs={'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'form-control', 'id': 'id_region'}),
            'tipo_inmueble': forms.Select(attrs={'class': 'form-control'}),
            'propietario': forms.Select(attrs={'class': 'form-control'}),
        }
        