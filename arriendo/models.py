from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Tipo_usuario(models.Model):
    nombre = models.CharField(max_length=20)
   
    def __str__(self):
        return f'{self.nombre}'

class Usuario (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=9,primary_key=True)
    direccion = models.CharField(max_length=50,null=True,blank=True)
    telefono = models.CharField(max_length=50,null=True,blank=True)
    tipo_usuario = models.ForeignKey(Tipo_usuario,on_delete=models.CASCADE,null=True,blank=True)
    # nombres=models.CharField(max_length=50,null=False,blank=False)
    # apellidos = models.CharField(max_length=50,null=False,blank=False)
    # correo = models.CharField(max_length=50,unique=True,null=False,blank=False)
    # contrasena=models.CharField(max_length=50,null=False,blank=False)
    
    
    def __str__(self):
        return f'{self.user.username}'


class Tipo_inmueble (models.Model):
    nombre = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.id} {self.nombre}'

class Region (models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.id} {self.nombre}'

class Comuna (models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region,on_delete=models.CASCADE,null=False)
    
    def __str__(self):
       return f'{self.id} {self.nombre}'
    
class Inmueble (models.Model):
    nombres=models.CharField(max_length=50,null=False,blank=False)
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_terreno = models.FloatField()
    nun_estacionamientos = models.IntegerField(default=0)
    num_habitaciones = models.IntegerField(default=0)
    num_banos = models.IntegerField(default=0)
    direccion = models.CharField(max_length=50,null=False,blank=False)
    precio_mensual = models.FloatField(null=False)
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE,null=False)
    region = models.ForeignKey(Region,on_delete=models.CASCADE,null=False)
    tipo_inmueble = models.ForeignKey(Tipo_inmueble,on_delete=models.CASCADE, null = False)
    propietario = models.ForeignKey(Usuario,on_delete=models.CASCADE,null=False)
    
class Estado_solicitud(models.Model):
    nombres=models.CharField(max_length=50,null=False,blank=False)
    
class Solicitud(models.Model):
    
    arrendatario = models.OneToOneField('Usuario', related_name="solicitudes",null= False,blank=False, on_delete=models.CASCADE )
    inmueble = models.OneToOneField('Inmueble', related_name="solicitudes",null= False,blank=False, on_delete=models.CASCADE )
    estado = models.OneToOneField('Estado_solicitud', related_name="solicitudes",null= False,blank=False, on_delete=models.CASCADE )
    fecha_solicitud = models.DateField(auto_now_add=True)
    
