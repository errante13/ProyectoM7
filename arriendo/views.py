import json
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from arriendo.models import Usuario,Inmueble,Comuna,Region,Tipo_inmueble
from arriendo.services import crear_usuario
from arriendo.forms import UsuarioForms,InmuebleForm
from django.contrib import messages


def index (request):
    regiones = Region.objects.all()
    tipo = Tipo_inmueble.objects.all()
    return render(request,'index.html',{ 'regiones':regiones,'tipo':tipo})


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

@login_required 
def actualizar(request):
    
    usuario = Usuario.objects.get(pk=request.user.usuario.rut)
    if request.method == "POST":
        form = UsuarioForms(request.POST, instance=usuario)
        
        if form.is_valid():
            form.save()
            messages.success(request,"datos actualizados Correctamente")
            return redirect('actualizar')  # Redirige a la vista de perfil o cualquier otra vista relevante

    else:
        form = UsuarioForms(instance=usuario)
        return render(request, 'ActualizarUsuario.html', {'form': form,'usuario': usuario})

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

def MostrarPropiedades(request):
     inmueble = Inmueble.objects.all()
     return render(request, 'MostrarPropiedades.html', {'inmueble':inmueble})

@login_required
def crearInmueble(request):
    if request.method == "POST":
        form = InmuebleForm(request.POST)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.propietario = Usuario.objects.get(pk=request.user.usuario.rut)
            inmueble.save()
            form.save()
            messages.success(request,"datos agregados Correctamente")
            return redirect('misPropiedades')  
    else:
        form = InmuebleForm()
        return render(request,'CrearInmueble.html',{'form':form})
  
def filtrar_comunas(request):
    region_id = request.GET.get('region')
    comunas = Comuna.objects.filter(region_id=region_id).all()
    return JsonResponse(list(comunas.values('id', 'nombre')), safe=False)

def MisPropiedades(request):
     inmueble = Inmueble.objects.filter(propietario=request.user.usuario.rut)
     return render(request, 'MisPropiedades.html', {'inmueble':inmueble})

def actualizarInmueble(request, id):
    inmueble = Inmueble.objects.get(pk=id)
    if request.method == "POST":
        if "save" in request.POST:
            form = InmuebleForm(request.POST, instance=inmueble)
            if form.is_valid():
                form.save()
                messages.success(request,"datos actualizados Correctamente")
                return redirect('misPropiedades') 
        elif "delete" in request.POST:
            inmueble.delete()
            messages.success(request,"Datos eliminados correctamente")
            return redirect('misPropiedades') 
    else:
        form = InmuebleForm(instance=inmueble)
        return render(request, 'inmuebleDetalle.html', {'form': form})
    
def buscarPor(request):
    
    idregion = request.POST["id_region"]
    idcomuna = request.POST["id_region"]
    idtipo = request.POST["tipo_inmueble"]
    
    if request.method == "POST":
        #region, comuna y tipo
        if idregion:
           inmueble = Inmueble.objects.filter(region = idregion)
           print(inmueble)
           return render(request, 'MostrarPropiedades.html', {'inmueble':inmueble})
        elif idtipo:
             inmueble = Inmueble.objects.filter(tipo_inmueble =idtipo)
             return render(request, 'MostrarPropiedades.html', {'inmueble':inmueble})
        elif idcomuna:
             inmueble = Inmueble.objects.filter(comuna =idcomuna)
             return render(request, 'MostrarPropiedades.html', {'inmueble':inmueble})
        #region y tipo 
        elif idregion and idtipo:
             inmueble = Inmueble.objects.filter(region =idregion,tipo_inmueble=idtipo)
             return render(request, 'MostrarPropiedades.html', {'inmueble':inmueble})
        
        #comuna y Tipo
        elif idcomuna and idtipo:
             inmueble = Inmueble.objects.filter(comuna =idcomuna,tipo_inmueble=idtipo)
             return render(request, 'MostrarPropiedades.html', {'inmueble':inmueble})
        else:
            inmueble = Inmueble.objects.all()
            return render(request, 'MostrarPropiedades.html',{'inmueble':inmueble})
    
   
   