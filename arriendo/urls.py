from django.urls import path
from arriendo.views import * #index,registrarse,actualizar,iniciarSesion,cerrarSesion,crearInmueble,filtrar_comunas

urlpatterns = [
    path('', index ,name='home'),
    path('registrarse', registrarse ,name='registrarse'),
    path('actualizar', actualizar ,name='actualizar'),
    path('login', iniciarSesion ,name='login'),
    path('logout', cerrarSesion ,name='logout'),
    path('inmueble/nuevo',crearInmueble, name='crearInmueble'),
    path('filtrar-comunas/', filtrar_comunas, name='filtrar_comunas'),
    path('inmueble',MostrarPropiedades , name='mostrarInmuebles'),
    path('inmueble/listar', MisPropiedades , name='misPropiedades'),
    path('inmueble/<int:id>/', actualizarInmueble , name='editarInmueble')
    
]
