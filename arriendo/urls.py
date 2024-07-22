from django.urls import path
from arriendo.views import index,registrarse,actualizar,iniciarSesion,cerrarSesion

urlpatterns = [
    path('', index ,name='home'),
    path('registrarse', registrarse ,name='registrarse'),
    path('actualizar', actualizar ,name='actualizar'),
    path('login', iniciarSesion ,name='login'),
    path('logout', cerrarSesion ,name='logout'),
    
]
