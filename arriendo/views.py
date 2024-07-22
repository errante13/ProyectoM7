from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from arriendo.models import Usuario
from arriendo.services import crear_usuario
from arriendo.forms import UsuarioForms
from django.contrib import messages


def index (request):
    return render(request,'index.html')


def registrarse (request):
    
    if request.method == "GET":
        return render(request,'RegistroUsuario.html')
    
    if request.method == "POST":
        username = request.POST["username"]
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        contrasena = request.POST["password"]
        email = request.POST["email"]
        telefono = request.POST["telefono"]
        rut = request.POST["rut"]
        direccion = request.POST["direccion"]
        crear_usuario(username,nombre,apellido,contrasena,email,telefono,rut,direccion)
        return redirect ("login")
 
def actualizar(request):
    
    usuario = Usuario.objects.get(pk=request.user.usuario.rut)
    user = request.user
    if request.method == "POST":
        form = UsuarioForms(request.POST, instance=usuario)
        
        if form.is_valid():
            form.save()
            messages.success(request,"datos actualizados Correctamente")
            return redirect('actualizar')  # Redirige a la vista de perfil o cualquier otra vista relevante

    else:
        form = UsuarioForms(instance=usuario)
        return render(request, 'ActualizarUsuario.html', {'form': form,'usuario': usuario, 'user':user})

def iniciarSesion(request):
    
    if request.method == 'GET':
        return render(request,'IniciarSesion.html')   
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'IniciarSesion.html', {"error": "Usuario o Contraseña es incorrecto."})
        else:
            login(request, user)
            return redirect('actualizar')
    

def cerrarSesion(request):
    
    logout(request)
    messages.info(request,"sesión cerrada con éxito")
    return redirect ('home') 

def perfil(request):
    
    usuario = Usuario.objects.get(pk=request.user.usuario.rut)
    return render(request, 'InfoPerfil.html', {'usuario': usuario})