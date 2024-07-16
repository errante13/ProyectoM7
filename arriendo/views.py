from django.shortcuts import render

# Create your views here.
# inmobiliaria/views.py

#----------------------------TESTING DE CODIGO -----------------------


# from django.http import JsonResponse
# from django.views.decorators.http import require_http_methods
# from .services import create_usuario, get_usuario, update_usuario, delete_usuario

# @require_http_methods(["POST"])
# def create_usuario_view(request):
#     data = request.POST
#     usuario = create_usuario(
#         nombres=data.get('nombres'),
#         apellidos=data.get('apellidos'),
#         rut=data.get('rut'),
#         direccion=data.get('direccion'),
#         telefono=data.get('telefono'),
#         correo=data.get('correo'),
#         tipo_usuario=data.get('tipo_usuario')
#     )
#     return JsonResponse({'id': usuario.id, 'nombres': usuario.nombres, 'apellidos': usuario.apellidos})

# Y así sucesivamente para las demás operaciones CRUD y modelos.
def index (request):
    return render('index.html')