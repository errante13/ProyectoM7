from django.contrib.auth.models import User
from .models import *
 
 
 #Usuario CRUD
 
def crear_usuario(username,nombre,apellido,contrasena,email,telefono,rut,direccion):
    #crea al user por defecto en el sistema
    user = User.objects.create_user(username, email, contrasena)
    user.first_name = nombre
    user.last_name= apellido
    user.save()
    #recuperar la instancia del tipo de usuario
    tipoUsuario = Tipo_usuario.objects.get(pk = 3)
    #crea al usuario personalizado
    usuario = Usuario(user=user,rut=rut,direccion=direccion,telefono=telefono,tipo_usuario=tipoUsuario)
    usuario.save()
    

def obtener_usuario(rut):
    return Usuario.objects.get(pk=rut)

def actualizar_usuario(nombres,apellidos,rut,direccion,correo,tipo,contrasena):
    usuario = obtener_usuario(pk=rut)
    if usuario:
       usuario = Usuario(nombres=nombres,apellidos=apellidos,direccion=direccion,correo=correo,tipo=tipo,contrasena=contrasena)
       usuario.save()
       return usuario
    else: 
        return "USUARIO NO ENCONTRADO"    
    
def borrar_usuario(rut):
    usuario = obtener_usuario(rut)
    if usuario:
        usuario.delete()
        return True
    return False    
    
#inmueble CRUD 

def crear_inmueble(nombre,descripcion,construido,terreno,estacionamiento,habitaciones,banos,direccion,precio,comuna,region,tipo,propietario):
    
    inmueble = Inmueble(nombres=nombre,descripcion=descripcion,m2_construidos=construido,m2_terreno=terreno,nun_estacionamientos=estacionamiento,num_habitaciones=habitaciones,num_banos=banos,direccion=direccion,precio_mensual=precio,comuna=comuna,region=region,tipo_inmueble=tipo,propietario=propietario)
    inmueble.save() 
    return inmueble

def obtener_inmueble(id):
    return Inmueble.objects.get(pk=id)

def actualizar_inmueble(id,nombre,descripcion,construido,terreno,estacionamiento,habitaciones,banos,direccion,precio,comuna,region,tipo,usuario):
    inmueble =obtener_inmueble(pk=id)
    if inmueble:
        Inmueble(nombres=nombre,descripcion=descripcion,m2_construidos=construido,m2_terreno=terreno,nun_estacionamientos=estacionamiento,num_habitaciones=habitaciones,num_banos=banos,direccion=direccion,precio_mensual=precio,comuna=comuna,region=region,tipo_inmueble=tipo,propietario=usuario)
        inmueble.save() 
        return inmueble
    else: 
        return "INMUEBLE NO ENCONTRADO"    
    
def borrar_inmueble(id):
    inmueble = obtener_inmueble(id)
    if inmueble:
        inmueble.delete()
        return True
    return False   

def listar_inmuebles():
    arriendos = Inmueble.objects.all()
    return arriendos

def listar_imnubles_x_comuna(comuna):
    arriendos = Inmueble.objects.filter(comuna=comuna)
    return arriendos

def listar_imnubles_x_usuario(rut):
    arriendos = Inmueble.objects.filter(propietario=rut)
    return arriendos

#solicitudes CRUD

def crear_solicitud(arrendatario, inmueble, estado='pendiente'):
    solicitud = Solicitud(arrendatario=arrendatario,inmueble=inmueble, estado=estado)
    solicitud.save()
    return solicitud

def obtener_solicitud(id_solicitud):
        return Solicitud.objects.get(id=id_solicitud)
    
def actualizar_solicitud(id_solicitud,arrendatario,inmueble,estado):
    solicitud = obtener_solicitud(id_solicitud)
    if solicitud:
        solicitud=Solicitud(arrendatario=arrendatario,inmueble=inmueble,estado=estado)
        solicitud.save()
        return solicitud
    else:
        return None
    
def borrar_solicitud(id_solicitud):
    solicitud = obtener_solicitud(id_solicitud)
    if solicitud:
        solicitud.delete()
        return True
    return False


# def get_raw_inmuebles_comuna():
#     query = """ select inmueble.nombres,inmueble.descripcion,comuna.nombre as comuna,region.nombre as region
#                 from arriendo_inmueble as inmueble
#                 inner join arriendo_region as region 
#                 on inmueble.region_id = region.id  
#                 inner join arriendo_comuna as comuna 
#                 on inmueble.comuna_id = comuna.id
#                 GROUP BY region.nombre, inmueble.id, inmueble.nombres, comuna.nombre
#                 order by comuna.nombre ;"""
#     listar_inmuebles = Inmueble.objects.raw(query)  
    
#     archivo = open('inmuebles_comuna.txt','w')
#     for inmueble in listar_inmuebles:
#         archivo.write(inmueble.nombre+','+inmueble.id+','+inmueble.comuna+','+inmueble.region+'\n')
#     archivo.close()


# def get_raw_inmuebles_regiones():
#     query = """ select inmueble.nombres,inmueble.descripcion,comuna.nombre as comuna,region.nombre as region
#                 from arriendo_inmueble as inmueble
#                 inner join arriendo_region as region 
#                 on inmueble.region_id = region.id  
#                 inner join arriendo_comuna as comuna 
#                 on inmueble.comuna_id = comuna.id
#                 GROUP BY region.nombre, inmueble.id, inmueble.nombres, comuna.nombre
#                 order by region.nombre ;"""
#     listar_inmuebles = Inmueble.objects.raw(query)  
    
#     archivo = open('inmuebles_regiones.txt','w')
#     for inmueble in listar_inmuebles:
#         archivo.write(inmueble.nombre+','+inmueble.id+','+inmueble.comuna+','+inmueble.region+'\n')
#     archivo.close()
