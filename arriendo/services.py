from .models import *
 
def listar_inmuebles():
    arriendos = Inmueble.objects.all()
    return arriendos

def listar_imnubles_comuna(comuna):
    arriendos = Inmueble.objects.filter(comuna=comuna)
    return arriendos

def listar_imnubles_by_rut(rut):
    arriendos = Inmueble.objects.filter(pk=rut)
    return arriendos

def crear_usuario(nombres,apellidos,rut,direccion,correo,tipo):
    usuario = Usuario(rut=rut,nombres=nombres,apellidos=apellidos,direccion=direccion,correo=correo,Tipo_usuario=tipo)
    usuario.save()


def actualizar_datos(nombres,apellidos,rut,direccion,correo,tipo):
    usuario = Usuario.objects.get(pk=rut)
    usuario = Usuario(nombres=nombres,apellidos=apellidos,direccion=direccion,correo=correo,Tipo_usuario=tipo)
    usuario.save()
    
def crear_arriendo(nombre,descripcion,construido,terreno,estacionamiento,habitaciones,banos,direccion,precio,comuna,region,tipo,usuario):
    inmueble = Inmueble(nombres=nombre,descripcion=descripcion,mts_construidos=construido,mts_terreno=terreno,nun_estacionamientos=estacionamiento,num_habitaciones=habitaciones,num_banos=banos,direccion=direccion,precio_mensual=precio,comuna=comuna,region=region,tipo_inmueble=tipo,usuario=usuario)
    inmueble.save()