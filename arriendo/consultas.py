from .models import *

def get_raw_inmuebles_comuna():
    query = """select inmueble.nombres,inmueble.descripcion,comuna.nombre as comuna,region.nombre as region 
               from arriendo_inmueble as inmueble 
               inner join arriendo_region as region 
               on inmueble.region_id = region.id  
               inner join arriendo_comuna as comuna 
               on inmueble.comuna_id = comuna.id 
               GROUP BY inmueble.nombres, inmueble.descripcion, comuna.nombre,region.nombre
               order by comuna.nombre;"""
    
    
    inmuebles = Inmueble.objects.raw(query)  
    print(inmuebles)
    archivo = open('inmuebles_comuna.txt','w')
    for inmueble in inmuebles:
        archivo.write(inmueble.nombres+','+ inmueble.descripcion +'\n')
    archivo.close()


def get_raw_inmuebles_regiones():
    query = """ select inmueble.nombres,inmueble.descripcion,comuna.nombre as comuna,region.nombre as region
                from arriendo_inmueble as inmueble
                inner join arriendo_region as region 
                on inmueble.region_id = region.id  
                inner join arriendo_comuna as comuna 
                on inmueble.comuna_id = comuna.id
                GROUP BY region.nombre, inmueble.id, inmueble.nombres, comuna.nombre
                order by region.nombre ;"""
    listar_inmuebles = Inmueble.objects.raw(query)  
    
    archivo = open('inmuebles_regiones.txt','w')
    for inmueble in listar_inmuebles:
        archivo.write(inmueble.nombre+','+inmueble.id+','+inmueble.comuna+','+inmueble.region+'\n')
    archivo.close()
