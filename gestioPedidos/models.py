import email
from email.errors import MalformedHeaderDefect
from pickle import TRUE
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion= models.CharField(max_length=50, verbose_name='La direccion')#cambiar como aparece nombre de campo con verbose name
    email=models.EmailField(blank=True, null=True)#campo opcional con blank
    telefono=models.CharField(max_length=11)

class Articulos(models.Model):
    nombre= models.CharField(max_length=30)
    seccion= models.CharField(max_length=20)
    precio= models.IntegerField()

    def __str__(self):
        return 'El nombre es %s la seccion es %s y el precio es %s' %(self.nombre, self.seccion, self.precio)

class Pedidos(models.Model):
    numero= models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()

class registro_autos(models.Model):
    marca=models.CharField(max_length=20)
    modelo=models.CharField(max_length=20)
    year=models.IntegerField()
    vin=models.CharField(max_length=17)
    placa=models.CharField(max_length=8)