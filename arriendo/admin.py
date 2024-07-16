from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Tipo_usuario)
admin.site.register(Tipo_inmueble)
admin.site.register(Inmueble)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Estado_solicitud)
admin.site.register(Solicitud)
