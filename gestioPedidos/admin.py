from pyexpat import model
from unicodedata import name
from django.contrib import admin
# poner los menus(modelo) en el dashboard
from gestioPedidos.models import Clientes, Articulos, Pedidos, registro_autos
#from tiendaOnline.gestioPedidos.views import registro_auto
# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display=('nombre', 'direccion', 'email', 'telefono')#campos a mostar como tablas
    search_fields=('nombre','email', 'telefono')


class ArticulosAdmin(admin.ModelAdmin):
    list_display=('nombre', 'seccion', 'precio')#campos a mostar como tablas
    search_fields=('nombre','seccion')
    list_filter=('seccion',)

class PedidosAdmin(admin.ModelAdmin):
    list_display=('numero', 'fecha', 'entregado')#campos a mostar como tablas
    search_fields=('numero',)#siempre coma al final si es solo un campo como parametro de busqueda
    list_filter=('fecha',)
    date_hierarchy='fecha'

class registroautosAdmin(admin.ModelAdmin):
    list_display=('marca', 'modelo', 'year','vin','placa')#campos a mostar como tablas
    search_fields=('placa',)#siempre coma al final si es solo un campo como parametro de busqueda
    #list_filter=('fecha',)
    #date_hierarchy='fecha'


admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Pedidos, PedidosAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(registro_autos, registroautosAdmin)
