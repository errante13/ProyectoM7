from django.db import models

# Create your models here.

class Tipo_usuario(models.Model):
    nombre = models.CharField(max_length=20)

class Usuario (models.Model):
    rut = models.CharField(max_length=9,primary_key=True)
    nombres=models.CharField(max_length=50,null=False,blank=False)
    apellidos = models.CharField(max_length=50,null=False,blank=False)
    direccion = models.CharField(max_length=50,null=False,blank=False)
    telefono = models.CharField(max_length=50,null=False,blank=False)
    correo = models.CharField(max_length=50,null=False,blank=False)
    tipo_usuario = models.ForeignKey(Tipo_usuario,on_delete=models.CASCADE,null=False)

class Tipo_inmueble (models.Model):
    nombre = models.CharField(max_length=20)

class Region (models.Model):
    nombre = models.CharField(max_length=30)

class Comuna (models.Model):
    nombre = models.CharField(max_length=20)
    region = models.ForeignKey(Region,on_delete=models.CASCADE,null=False)
    
class Inmueble (models.Model):
    nombres=models.CharField(max_length=50,null=False,blank=False)
    descripcion = models.TextField()
    mts_construidos = models.FloatField()
    mts_terreno = models.FloatField()
    nun_estacionamientos = models.IntegerField(default=0)
    num_habitaciones = models.IntegerField(default=0)
    num_banos = models.IntegerField(default=0)
    direccion = models.CharField(max_length=50,null=False,blank=False)
    precio_mensual = models.FloatField(null=False)
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE,null=False)
    region = models.ForeignKey(Region,on_delete=models.CASCADE,null=False)
    tipo_inmueble = models.ForeignKey(Tipo_inmueble,on_delete=models.CASCADE, null = False)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,null=False)
    
    
    
    
    
