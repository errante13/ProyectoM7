from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

admin.site.register(Usuario)

class Tipo_usuario_Admin(admin.ModelAdmin):
      list_display = ('id', 'nombre')
admin.site.register(Tipo_usuario,Tipo_usuario_Admin)

admin.site.register(Tipo_inmueble)
admin.site.register(Inmueble)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Estado_solicitud)
admin.site.register(Solicitud)
