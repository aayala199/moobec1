from django.http import HttpResponse
from django.shortcuts import render
from gestioPedidos.models import Articulos

# Create your views here.
def busqueda_productos(request):
    return render(request,'busqueda_productos.html')

def buscar_productos(request):
    if request.GET['prd']:
        #mensaje='marca: %r exitosamente ' %request.GET['marca_vehiculo']
        producto=request.GET['prd']
        articulos=Articulos.objects.filter(nombre__icontains=producto)
        return render(request, "respuesta_producto.html", {"articulos": articulos, "query":producto})
    else:
        mensaje='no has introducido nada'

    return HttpResponse(mensaje)

def home(request):
    return render(request,'home.html')

def registro_auto(request):
    if request.method=="POST":
        return render(request, "gracias.html")
    return render(request, "registro_auto.html")