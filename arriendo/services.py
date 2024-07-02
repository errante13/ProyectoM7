from .models import *
 
def listar_inmuebles():
    arriendos = Inmueble.objects.all()
    return arriendos